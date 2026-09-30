## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-80.0.0.0.0
-  __TEXT.__text: 0x72604
+81.0.0.0.0
+  __TEXT.__text: 0x72720
   __TEXT.__objc_methlist: 0xa8c
   __TEXT.__const: 0x5bf8
-  __TEXT.__cstring: 0x68aa
+  __TEXT.__cstring: 0x68da
   __TEXT.__oslogstring: 0x21e3
   __TEXT.__gcc_except_tab: 0x1dc
   __TEXT.__dlopen_cstrs: 0x74

   __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__got: 0x558
   __AUTH_CONST.__const: 0x4cb0
-  __AUTH_CONST.__cfstring: 0x55e0
+  __AUTH_CONST.__cfstring: 0x5620
   __AUTH_CONST.__objc_const: 0x1910
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH_CONST.__auth_got: 0x1140
   __AUTH.__objc_data: 0x7e8
   __AUTH.__data: 0x448
   __DATA.__objc_ivar: 0xc8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2226
-  Symbols:   1729
-  CStrings:  1083
+  Symbols:   1728
+  CStrings:  1085
 
Symbols:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$seekToOffset:error:
- _objc_msgSend$availableData
- _objc_msgSend$seekToFileOffset:
- _objc_retain_x27
Functions:
~ +[ReportViewerObjC transformURL:template:options:] : 2396 -> 2680
CStrings:
+ "Unable to read log stream: %@"
+ "unknown error"
```
