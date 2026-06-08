## libAHTRestore.dylib

> `/usr/lib/libAHTRestore.dylib`

```diff

-9140.6.0.0.0
-  __TEXT.__text: 0x193c
-  __TEXT.__auth_stubs: 0x280
+10100.34.0.0.0
+  __TEXT.__text: 0x1878
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x254
+  __TEXT.__cstring: 0x257
   __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0xc
-  __TEXT.__objc_methname: 0x467
-  __TEXT.__objc_methtype: 0x9b
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x190
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90714D64-E6F2-3976-95CC-83C3B76AAE4E
+  UUID: 0F809A26-2A65-32C9-A9F8-6DFABE206B96
   Functions: 31
-  Symbols:   180
-  CStrings:  147
+  Symbols:   184
+  CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[AHTLoader allDevices] : 372 -> 360
~ ___23+[AHTLoader allDevices]_block_invoke : 128 -> 132
~ +[AHTLoader withName:] : 356 -> 348
~ +[AHTLoader bootloaderPropertiesForImageTag:] : 280 -> 272
~ -[AHTLoader description] : 192 -> 184
~ -[AHTLoader fullDescription] : 648 -> 608
~ ___28-[AHTLoader fullDescription]_block_invoke : 84 -> 80
~ ___28-[AHTLoader fullDescription]_block_invoke_2 : 420 -> 392
~ +[AHTLoader errorFromKernel:error:] : 276 -> 264
~ +[AHTLoader errorFromAfuKextResult:error:] : 308 -> 296
~ -[AHTLoader loadImage:payloadOnly:options:error:] : 536 -> 516
~ -[AHTLoader overrideFDR:fdrClass:fdrSubclass:error:] : 448 -> 456
~ -[AHTLoader overrideNextLoadOptions:error:] : 120 -> 116
~ +[AHTLoader registryPropertiesForService:] : 92 -> 88
~ _AHTRestoreCreateDeviceList : 528 -> 508
~ _AHTRestoreUpdateDevice : 200 -> 196
~ _AHTRestoreUpdateDeviceWithOverrides : 504 -> 484
~ _AHTRestoreFailureCleanup : 192 -> 188
CStrings:
+ "AIDFirmwareUpdateService"
- ".cxx_destruct"
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "AHTLoader"
- "AppleFirmwareUpdateKext"
- "B24@0:8^@16"
- "B28@0:8i16^@20"
- "B32@0:8Q16^@24"
- "B44@0:8@16B24Q28^@36"
- "B48@0:8@16@24@32^@40"
- "I"
- "I16@0:8"
- "T@\"NSString\",R,N,V_name"
- "TI,N,V_connect"
- "TI,N,V_service"
- "TI,R,N,V_imageTag"
- "TI,R,N,V_loadingGroup"
- "UTF8String"
- "_connect"
- "_imageTag"
- "_loadingGroup"
- "_name"
- "_service"
- "addObject:"
- "allDevices"
- "appendData:"
- "arrayWithObjects:count:"
- "bootloaderPropertiesForImageTag:"
- "bytes"
- "close"
- "code"
- "connect"
- "countByEnumeratingWithState:objects:count:"
- "dataUsingEncoding:"
- "dealloc"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "errorFromAfuKextResult:error:"
- "errorFromKernel:error:"
- "errorWithDomain:code:userInfo:"
- "fullDescription"
- "imageTag"
- "init"
- "initWithCapacity:"
- "initWithService:"
- "intValue"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "length"
- "loadImage:payloadOnly:options:error:"
- "loadingGroup"
- "name"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "open:"
- "overrideFDR:fdrClass:fdrSubclass:error:"
- "overrideNextLoadOptions:error:"
- "registryPropertiesForService:"
- "service"
- "setConnect:"
- "setService:"
- "sortDescriptorWithKey:ascending:comparator:"
- "sortUsingDescriptors:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8I16"
- "withName:"
- "withService:"

```
