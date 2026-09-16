## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

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
-  __TEXT.__text: 0x19654
+382.100.2.0.0
+  __TEXT.__text: 0x19658
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x2280
   __TEXT.__objc_methlist: 0x9ac
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x12e6
+  __TEXT.__cstring: 0x1303
   __TEXT.__oslogstring: 0x2571
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x25f1
+  __TEXT.__objc_methname: 0x25fa
   __TEXT.__objc_methtype: 0x67b
   __TEXT.__gcc_except_tab: 0x1274
   __TEXT.__unwind_info: 0x568
   __DATA_CONST.__const: 0x348
-  __DATA_CONST.__cfstring: 0x1920
+  __DATA_CONST.__cfstring: 0x1940
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_selrefs: 0xa90
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x400
+  __DATA.__data: 0x408
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   Functions: 311
-  Symbols:   965
-  CStrings:  879
+  Symbols:   966
+  CStrings:  880
 
Symbols:
+ _kANEFModelMutableClusterIndexKey
+ _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:
- _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:
Functions:
~ ___161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke : 7496 -> 7500
CStrings:
+ "ANEFModelMutableClusterIndex"
+ "cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:"
- "cloneIfWritable:isEncryptedModel:cloneDirectory:"
```
