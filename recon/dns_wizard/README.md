# recon - dns_wizard

## Challenge
Can you find it?

made by: acurless

## Solution
```
➜  host -t TXT wpictf.xyz
wpictf.xyz descriptive text "V1BJezFGMHVuZF9UaDNfRE5TLXJlY29yZH0="
➜  echo V1BJezFGMHVuZF9UaDNfRE5TLXJlY29yZH0= | base64 -D
WPI{1F0und_Th3_DNS-record}%
```

## Flag
```
WPI{1F0und_Th3_DNS-record}
```
