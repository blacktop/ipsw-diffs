## libicucore.A.dylib

> `/usr/lib/libicucore.A.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`

```diff

-78128.0.0.0.0
-  __TEXT.__text: 0x26a990
+78131.0.0.0.0
+  __TEXT.__text: 0x26a8fc
   __TEXT.__const: 0x6b3c0
-  __TEXT.__cstring: 0xa17e
+  __TEXT.__cstring: 0xa179
   __TEXT.__oslogstring: 0xf0
   __TEXT.__ustring: 0x2a88
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 12208
   Symbols:   8966
-  CStrings:  4170
+  CStrings:  4169
 
Functions:
~ __ZNK3icu16SimpleDateFormat9subFormatERNS_13UnicodeStringEDsi15UDisplayContextiDsRNS_20FieldPositionHandlerERNS_8CalendarER10UErrorCode : 6832 -> 6804
~ __ZN3icu16SimpleDateFormat22getPatternForTimeStyleENS_10DateFormat6EStyleERKNS_6LocaleEP15UResourceBundleRNS_13UnicodeStringER10UErrorCode : 840 -> 804
~ __ZN3icu24DateTimePatternGenerator24localeUsesLongDayPeriodsERKNS_6LocaleE : 388 -> 292
~ sub_18f6c4c88 -> sub_18f827be8 : 80 -> 92
CStrings:
- "ldpn"
```
