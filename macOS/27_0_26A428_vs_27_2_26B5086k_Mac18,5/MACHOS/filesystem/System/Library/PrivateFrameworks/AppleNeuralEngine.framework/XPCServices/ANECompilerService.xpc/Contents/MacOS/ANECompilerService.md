## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/Contents/MacOS/ANECompilerService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x1bffc
+382.100.0.0.0
+  __TEXT.__text: 0x1bff8
   __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x9b4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x1366
+  __TEXT.__cstring: 0x1383
   __TEXT.__oslogstring: 0x267e
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x2644
+  __TEXT.__objc_methname: 0x264d
   __TEXT.__objc_methtype: 0x67b
   __TEXT.__gcc_except_tab: 0x12d4
   __TEXT.__unwind_info: 0x5d8
   __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0x1980
+  __DATA_CONST.__cfstring: 0x19a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_selrefs: 0xaa8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x400
+  __DATA.__data: 0x408
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   Functions: 343
-  Symbols:   968
-  CStrings:  897
+  Symbols:   969
+  CStrings:  898
 
Symbols:
+ _kANEFModelMutableClusterIndexKey
+ _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:
- _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:
Functions:
~ ___161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke : 7916 -> 7912
CStrings:
+ "ANEFModelMutableClusterIndex"
+ "cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:"
- "cloneIfWritable:isEncryptedModel:cloneDirectory:"
```
