## iMessageLite

> `/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`

```diff

-1491.300.43.0.0
-  __TEXT.__text: 0x4f0ac
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0x2640
-  __TEXT.__objc_methlist: 0x404
+1491.300.74.0.0
+  __TEXT.__text: 0x4f388
+  __TEXT.__auth_stubs: 0x1870
+  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_methlist: 0x46c
   __TEXT.__const: 0x2908
-  __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__cstring: 0x10b7
+  __TEXT.__gcc_except_tab: 0x1e0
+  __TEXT.__cstring: 0x1117
   __TEXT.__oslogstring: 0x25c4
-  __TEXT.__objc_classname: 0x1ed
-  __TEXT.__objc_methtype: 0x7c6
-  __TEXT.__objc_methname: 0x2801
+  __TEXT.__objc_classname: 0x1fd
+  __TEXT.__objc_methtype: 0x7d6
+  __TEXT.__objc_methname: 0x2931
   __TEXT.__dlopen_cstrs: 0x44
   __TEXT.__swift5_typeref: 0xbd0
   __TEXT.__constg_swiftt: 0x7d8

   __TEXT.__swift_as_cont: 0x230
   __TEXT.__swift5_assocty: 0x130
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1568
+  __TEXT.__unwind_info: 0x1590
   __TEXT.__eh_frame: 0x3268
-  __DATA_CONST.__const: 0x2840
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x2868
+  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0x670
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xc48
+  __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x500
-  __DATA.__objc_const: 0xb08
-  __DATA.__objc_selrefs: 0xad0
-  __DATA.__objc_data: 0xc0
-  __DATA.__data: 0xbf8
+  __DATA.__objc_const: 0xc50
+  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x110
+  __DATA.__data: 0xbf0
   __DATA.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
-  - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence
   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1282
-  Symbols:   3989
-  CStrings:  717
+  Functions: 1294
+  Symbols:   4022
+  CStrings:  735
 
Symbols:
+ +[IMLitePluginPayload imCoreBundle]
+ +[IMLitePluginPayload pluginBundleIDForBalloonBundleID:]
+ -[IMLitePluginPayload .cxx_destruct]
+ -[IMLitePluginPayload data]
+ -[IMLitePluginPayload initWithMessageItem:]
+ -[IMLitePluginPayload pluginBundleID]
+ -[IMLitePluginPayload url]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MessagesCore/install/TempContent/Objects/iMessageLite.build/iMessageLite.build/Objects-normal/arm64e/IMLitePluginPayload.o
+ IMLitePluginPayload.m
+ _$sSo12NSDictionaryCMa
+ _$sSo13IMMessageItemC12iMessageLiteE12imCoreString33_1BC1E26FF7EAE316FD1B216EFFD0ADEELL6forKeySSSgSS_tFTf4nd_n
+ _$sSo13IMMessageItemC12iMessageLiteE7summary33_1BC1E26FF7EAE316FD1B216EFFD0ADEELL4fromSSSgSo19IMLitePluginPayloadC_tFTf4nd_n
+ _IMBalloonBundleIdentifierAskTo
+ _IMBalloonBundleIdentifierLegacyAskToBuy
+ _IMBalloonBundleIdentifierLegacyScreenTime
+ _IMLinkAttributeName
+ _OBJC_CLASS_$_IMLitePluginPayload
+ _OBJC_CLASS_$_NSObject
+ _OBJC_IVAR_$_IMLitePluginPayload._data
+ _OBJC_IVAR_$_IMLitePluginPayload._pluginBundleID
+ _OBJC_IVAR_$_IMLitePluginPayload._url
+ _OBJC_METACLASS_$_IMLitePluginPayload
+ __OBJC_$_CLASS_METHODS_IMLitePluginPayload
+ __OBJC_$_CLASS_PROP_LIST_IMLitePluginPayload
+ __OBJC_$_INSTANCE_METHODS_IMLitePluginPayload
+ __OBJC_$_INSTANCE_VARIABLES_IMLitePluginPayload
+ __OBJC_$_PROP_LIST_IMLitePluginPayload
+ __OBJC_CLASS_RO_$_IMLitePluginPayload
+ __OBJC_METACLASS_RO_$_IMLitePluginPayload
+ ___43-[IMLitePluginPayload initWithMessageItem:]_block_invoke
+ ___block_descriptor_40_e8_32r_e34_v40?0"NSURL"8{_NSRange=QQ}16^B32lr32l8
+ _objc_msgSend$_FTOptionallyDecompressData
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
+ _objc_msgSend$imCoreBundle
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isUpgradedAskToBuyEnabled
+ _objc_msgSend$pluginBundleIDForBalloonBundleID:
+ _objc_storeStrong
+ _swift_retain_x23
- _$sSo12NSDictionaryCMaTm
- _$sSo13IMMessageItemC12iMessageLiteE7summary33_1BC1E26FF7EAE316FD1B216EFFD0ADEELL4fromSSSgSo15IMPluginPayloadC_tFTf4nd_n
- _$sSo6IMChatCML
- _OBJC_CLASS_$_IMChat
- _OBJC_CLASS_$_IMPluginPayload
- _objc_msgSend$bundleForClass:
- _swift_retain_x24
CStrings:
+ "/System/Library/PrivateFrameworks/IMCore.framework"
+ "@\"NSData\""
+ "@\"NSString\""
+ "@\"NSURL\""
+ "IMLitePluginPayload"
+ "T@\"NSBundle\",R,N"
+ "T@\"NSData\",R,N,V_data"
+ "T@\"NSString\",R,N,V_pluginBundleID"
+ "T@\"NSURL\",R,N,V_url"
+ "_FTOptionallyDecompressData"
+ "_pluginBundleID"
+ "_url"
+ "bundleWithPath:"
+ "enumerateAttribute:inRange:options:usingBlock:"
+ "imCoreBundle"
+ "isEqualToString:"
+ "isUpgradedAskToBuyEnabled"
+ "pluginBundleIDForBalloonBundleID:"
+ "v40@?0@\"NSURL\"8{_NSRange=QQ}16^B32"
- "bundleForClass:"
```
