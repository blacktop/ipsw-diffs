## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0xffa8
+11.0.0.0.0
+  __TEXT.__text: 0x10000
   __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xec
-  __TEXT.__cstring: 0x14cc
+  __TEXT.__cstring: 0x14aa
   __TEXT.__oslogstring: 0x1d9e
   __TEXT.__gcc_except_tab: 0x394
   __TEXT.__unwind_info: 0x478

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__cfstring: 0x1220
   __AUTH_CONST.__objc_const: 0x19d0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 456
-  Symbols:   1149
-  CStrings:  302
+  Symbols:   1150
+  CStrings:  301
 
Symbols:
+ _objc_msgSend$sharedMonitor
Functions:
~ _refreshPreferences : 172 -> 260
CStrings:
- "ApplicationFirstFramePresentation"
```
