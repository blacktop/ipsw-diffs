## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Versions/A/Sentry`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0x1b6b8
+11.0.0.0.0
+  __TEXT.__text: 0x1b71c
   __TEXT.__objc_methlist: 0x1778
   __TEXT.__const: 0x174
   __TEXT.__cstring: 0x1ea8
   __TEXT.__oslogstring: 0x3043
   __TEXT.__gcc_except_tab: 0x3f4
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 765
-  Symbols:   1807
+  Symbols:   1808
   CStrings:  516
 
Symbols:
+ _objc_msgSend$sharedMonitor
Functions:
~ _refreshPreferences : 184 -> 284
```
