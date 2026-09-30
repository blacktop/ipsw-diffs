## CallKit

> `/System/Library/Frameworks/CallKit.framework/Versions/A/CallKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1395.100.1.0.0
-  __TEXT.__text: 0x6b9fc
-  __TEXT.__objc_methlist: 0x912c
+1397.100.1.0.0
+  __TEXT.__text: 0x6bbe4
+  __TEXT.__objc_methlist: 0x9154
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x62cc
-  __TEXT.__oslogstring: 0x38f1
+  __TEXT.__oslogstring: 0x3955
   __TEXT.__gcc_except_tab: 0x690
-  __TEXT.__unwind_info: 0x1cd0
+  __TEXT.__unwind_info: 0x1ce0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3450
+  __DATA_CONST.__objc_selrefs: 0x3468
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3230
-  Symbols:   6840
-  CStrings:  979
+  Functions: 3234
+  Symbols:   6847
+  CStrings:  980
 
Symbols:
+ -[CXChannelProvider _registerCurrentConfigurationIfAudioSessionIDStaleOnQueue]
+ -[CXChannelProvider _registerCurrentConfigurationOnQueue]
+ -[CXChannelProvider currentOpaqueAudioSessionID]
+ GCC_except_table65
+ ___35-[CXChannelProvider performAction:]_block_invoke
+ ___57-[CXChannelProvider _registerCurrentConfigurationOnQueue]_block_invoke
+ _objc_msgSend$_registerCurrentConfigurationIfAudioSessionIDStaleOnQueue
+ _objc_msgSend$_registerCurrentConfigurationOnQueue
+ _objc_msgSend$currentOpaqueAudioSessionID
- GCC_except_table61
- __49-[CXChannelProvider registerCurrentConfiguration]_block_invoke
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vtQtZb/Sources/CallKit/CallKit/CXCallDirectoryLabeledPhoneNumberEntryData.m"
+ "Cached audioSessionID %u no longer matches current opaqueSessionID %u; re-registering configuration"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ldmTbf/Sources/CallKit/CallKit/CXCallDirectoryLabeledPhoneNumberEntryData.m"
```
