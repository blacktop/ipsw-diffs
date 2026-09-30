## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/Versions/A/CoreDiagnostics`

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
-  __TEXT.__text: 0x77358
+81.0.0.0.0
+  __TEXT.__text: 0x774e4
   __TEXT.__objc_methlist: 0xa8c
   __TEXT.__const: 0x5c19
-  __TEXT.__cstring: 0x6737
+  __TEXT.__cstring: 0x6767
   __TEXT.__oslogstring: 0x24b2
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__constg_swiftt: 0x154c

   __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__got: 0x580
   __AUTH_CONST.__const: 0x4d68
-  __AUTH_CONST.__cfstring: 0x52c0
+  __AUTH_CONST.__cfstring: 0x5300
   __AUTH_CONST.__objc_const: 0x1910
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x1c8

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2255
   Symbols:   1713
-  CStrings:  1070
+  CStrings:  1072
 
Symbols:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$seekToOffset:error:
- _objc_msgSend$availableData
- _objc_msgSend$seekToFileOffset:
Functions:
~ +[ReportViewerObjC transformURL:template:options:] : 2564 -> 2960
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "Unable to read log stream: %@"
+ "unknown error"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
```
