## libicucore.A.dylib

> `/usr/lib/libicucore.A.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

-78128.0.0.0.0
-  __TEXT.__text: 0x269c18
+78131.0.0.0.0
+  __TEXT.__text: 0x269b7c
   __TEXT.__const: 0x6b3a0
-  __TEXT.__cstring: 0xa172
+  __TEXT.__cstring: 0xa16d
   __TEXT.__oslogstring: 0xf0
   __TEXT.__ustring: 0x2a88
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 12320
   Symbols:   9032
-  CStrings:  4170
+  CStrings:  4169
 
Functions:
~ sub_18471b2f0 -> sub_18485e2f0 : 80 -> 92
~ __ZN3icu24DateTimePatternGenerator24localeUsesLongDayPeriodsERKNS_6LocaleE : 388 -> 292
~ __ZN3icu16SimpleDateFormat22getPatternForTimeStyleENS_10DateFormat6EStyleERKNS_6LocaleEP15UResourceBundleRNS_13UnicodeStringER10UErrorCode : 840 -> 804
~ __ZNK3icu16SimpleDateFormat9subFormatERNS_13UnicodeStringEDsi15UDisplayContextiDsRNS_20FieldPositionHandlerERNS_8CalendarER10UErrorCode : 6832 -> 6796
CStrings:
- "ldpn"
```
