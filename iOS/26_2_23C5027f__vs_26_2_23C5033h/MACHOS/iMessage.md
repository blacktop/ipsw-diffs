## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.300.16.2.4
-  __TEXT.__text: 0xbb8f4
-  __TEXT.__auth_stubs: 0x1b40
+1450.300.27.0.0
+  __TEXT.__text: 0xbb77c
+  __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0xc4e0
-  __TEXT.__objc_methlist: 0x2b74
+  __TEXT.__objc_methlist: 0x2b84
   __TEXT.__const: 0xe68
-  __TEXT.__gcc_except_tab: 0xabd4
+  __TEXT.__gcc_except_tab: 0xaa1c
   __TEXT.__cstring: 0x34bd
-  __TEXT.__oslogstring: 0x16c5b
+  __TEXT.__oslogstring: 0x16e2b
   __TEXT.__objc_classname: 0x548
-  __TEXT.__objc_methname: 0x1268e
-  __TEXT.__objc_methtype: 0x29d5
+  __TEXT.__objc_methname: 0x1272b
+  __TEXT.__objc_methtype: 0x2a3c
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x676
   __TEXT.__constg_swiftt: 0x368

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x22d0
+  __TEXT.__unwind_info: 0x22a8
   __TEXT.__eh_frame: 0x8d8
-  __DATA_CONST.__auth_got: 0xdb0
+  __DATA_CONST.__auth_got: 0xdd8
   __DATA_CONST.__got: 0x1030
   __DATA_CONST.__auth_ptr: 0x1c8
-  __DATA_CONST.__const: 0x38a8
+  __DATA_CONST.__const: 0x38d0
   __DATA_CONST.__cfstring: 0x3820
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3240
-  __DATA.__objc_selrefs: 0x3a30
+  __DATA.__objc_const: 0x3248
+  __DATA.__objc_selrefs: 0x3a38
   __DATA.__objc_ivar: 0x208
   __DATA.__objc_data: 0xa58
   __DATA.__data: 0xa58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E5935D56-3DC7-356A-9E1B-1BE92967784B
-  Functions: 1662
-  Symbols:   866
-  CStrings:  5096
+  UUID: AD2F363D-4EC1-3F9E-A847-7EE25043D1F7
+  Functions: 1665
+  Symbols:   872
+  CStrings:  5110
 
Symbols:
+ _IMAcceptChatLogHandle
+ _IMFilterJunkLogHandle
+ _IMMarkAsReviewedLogHandle
+ _IMMarkUnreadLogHandle
+ _IMRecoverJunkLogHandle
+ __LastAddressedURIForChatWithMessageGUID
CStrings:
+ "  Reflect mark as reviewed for chat guids to peer devices using callerID: %@ account login ID: %@"
+ "  Unable to reflect accept chat, no caller id."
+ "  Unable to reflect junk chat, no caller id."
+ "  Unable to reflect mark as reviewed for chat guids, device is not registered for account: %@, bailing."
+ "  Unable to reflect mark unread, no caller id."
+ "  Unable to reflect recover junk chat, no caller id."
+ "?3D"
+ "?5A"
+ "?7@"
+ "?9@"
+ "?9A"
+ "?<B"
+ "@36@0:8Q16B24B28B32"
+ "@44@0:8Q16Q24B32B36B40"
+ "@56@0:8@16Q24Q32B40B44B48B52"
+ "@64@0:8Q16Q24Q32B40B44B48B52q56"
+ "Checking if local handle '%@' is in registered URIs: %@"
+ "Found matching alias: %@"
+ "Invalid guid"
+ "Local handle '%@' not found in registered URIs"
+ "No handle provided to find matching URI"
+ "No message found for message GUID '%@' or no destinationCallerID"
+ "No service."
+ "_bestGuessURIFromCanicalizedID"
+ "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:forceAutoDownloadIfPossible:lqmEnabled:isEncrypted:"
+ "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:lqmEnabled:isEncrypted:"
+ "encrypted"
+ "initForServiceName:limitType:limitSize:qualityType:isSticker:lowQualityModeEnabled:isEncrypted:"
+ "initWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:isEncrypted:restrictionReason:"
+ "noSpaceForHighQualityLimit:qualityType:isSticker:lqmEnabled:isEncrypted:"
+ "noSpaceForLowQualityLimit:qualityType:isSticker:lqmEnabled:isEncrypted:"
+ "restrictionAllowedBySettingWithQualityType:isSticker:lqmEnabled:isEncrypted:"
+ "restrictionDisallowedBySettingWithQualityType:isSticker:lqmEnabled:isEncrypted:"
+ "restrictionForceAllowedWithQualityType:isSticker:lqmEnabled:isEncrypted:"
+ "restrictionWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:isEncrypted:restrictionReason:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "  Reflect mark as reviewed for chat guids: %@ to peer devices using callerID: %@"
- "  Unable to reflect mark as reviewed for chat guids (%@), device is not registered for account: %@, bailing."
- "?4D"
- "?6A"
- "?8@"
- "?:@"
- "?:A"
- "?=B"
- "@32@0:8Q16B24B28"
- "@40@0:8Q16Q24B32B36"
- "@48@0:8@16Q24Q32B40B44"
- "@60@0:8Q16Q24Q32B40B44B48q52"
- "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:forceAutoDownloadIfPossible:lqmEnabled:"
- "_downloadRestrictionForUTIType:fileSize:qualityType:isSticker:lqmEnabled:"
- "callerURIForMessageGUID:idsAccount:"
- "initForServiceName:limitType:limitSize:qualityType:isSticker:lowQualityModeEnabled:"
- "initWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:restrictionReason:"
- "noSpaceForHighQualityLimit:qualityType:isSticker:lqmEnabled:"
- "noSpaceForLowQualityLimit:qualityType:isSticker:lqmEnabled:"
- "noteItemProcessed:batchContext:"
- "restrictionAllowedBySettingWithQualityType:isSticker:lqmEnabled:"
- "restrictionDisallowedBySettingWithQualityType:isSticker:lqmEnabled:"
- "restrictionForceAllowedWithQualityType:isSticker:lqmEnabled:"
- "restrictionWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:restrictionReason:"

```
