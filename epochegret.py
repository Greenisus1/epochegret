#!/usr/bin/env python3
"""Epochegret: exact UTC Unix seconds/milliseconds and offset ISO conversions."""
import argparse,datetime as d,json,re,sys
EPOCH=d.datetime(1970,1,1,tzinfo=d.timezone.utc)
def from_epoch(value,unit='s'):
    if unit not in ('s','ms'):raise ValueError('Use s or ms.')
    if not re.fullmatch(r'[+-]?\d{1,18}',value.strip(),flags=re.ASCII):raise ValueError('Enter integer epoch, up to 18 digits.')
    n=int(value);return EPOCH+d.timedelta(microseconds=n*(1000 if unit=='ms' else 1000000))
def parse_iso(value):
    value=value.strip()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})',value,flags=re.ASCII):raise ValueError('Use ISO date/time with seconds and Z or ±HH:MM offset.')
    offset=value[-6:]
    if offset[0] in '+-' and (int(offset[1:3])>23 or int(offset[4:6])>59):raise ValueError('Offset outside allowed range.')
    return d.datetime.fromisoformat(value[:-1]+'+00:00' if value.endswith('Z') else value).astimezone(d.timezone.utc)
def report(instant):
    if instant.tzinfo is None:raise ValueError('Timezone required.')
    instant=instant.astimezone(d.timezone.utc);delta=instant-EPOCH;us=(delta.days*86400+delta.seconds)*1000000+delta.microseconds
    return {'utc_iso':instant.isoformat(timespec='microseconds').replace('+00:00','Z'),'epoch_seconds':us//1000000 if us%1000000==0 else None,'epoch_milliseconds':us//1000 if us%1000==0 else None,'epoch_microseconds':us,'note':'Null means not exactly representable as an integer in that unit; no rounding.'}
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');a=p.parse_args(argv)
    try:
        print('EPOCHEGRET | explicit UTC/offsets, no local-time guessing',file=sys.stderr)
        print('1 Epoch seconds / 2 Epoch milliseconds / 3 Offset ISO / 0 Exit: ',end='',file=sys.stderr);mode=input().strip()
        if mode=='0':return 0
        if mode not in ('1','2','3'):raise ValueError('Choose 1, 2, 3 or 0.')
        print('Value: ',end='',file=sys.stderr);v=input();r=report(parse_iso(v) if mode=='3' else from_epoch(v,'s' if mode=='1' else 'ms'))
        if a.json:print(json.dumps(r,indent=2))
        else:
            for k,v in r.items():print(k+':',v)
    except (ValueError,OverflowError):print('Invalid value or outside Python datetime year range 1..9999.',file=sys.stderr);return 2
    except (EOFError,KeyboardInterrupt):print('\nCancelled.',file=sys.stderr)
    return 0
if __name__=='__main__':raise SystemExit(main())
