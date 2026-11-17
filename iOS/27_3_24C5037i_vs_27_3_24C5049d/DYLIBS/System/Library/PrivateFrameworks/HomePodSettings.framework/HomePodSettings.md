## HomePodSettings

> `/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`

```diff

-346.20.14.0.0
-  __TEXT.__text: 0x6d7a8
-  __TEXT.__objc_methlist: 0x1ffc
+346.20.19.0.0
+  __TEXT.__text: 0x6de80
+  __TEXT.__objc_methlist: 0x210c
   __TEXT.__const: 0x5430
-  __TEXT.__cstring: 0x2e91
+  __TEXT.__cstring: 0x2f91
   __TEXT.__oslogstring: 0x1119
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x1c0

   __TEXT.__swift_as_ret: 0x170
   __TEXT.__swift_as_cont: 0x3cc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3368
+  __TEXT.__unwind_info: 0x3398
   __TEXT.__eh_frame: 0x4970
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb90
-  __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_selrefs: 0xbf0
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__got: 0x4c0
   __AUTH_CONST.__const: 0x3aa0
-  __AUTH_CONST.__cfstring: 0x13c0
-  __AUTH_CONST.__objc_const: 0x64c0
+  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__objc_const: 0x6b48
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xfe8
-  __AUTH.__objc_data: 0x1e20
+  __AUTH_CONST.__auth_got: 0xff0
+  __AUTH.__objc_data: 0x1ec0
   __AUTH.__data: 0xd68
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x1bb8
+  __DATA.__objc_ivar: 0xe8
+  __DATA.__data: 0x1c18
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4117
-  Symbols:   2304
-  CStrings:  419
+  Functions: 4138
+  Symbols:   2357
+  CStrings:  427
 
Symbols:
+ +[HPSSiriRestrictions supportsSecureCoding]
+ -[HPSSiriRestrictions allowsBroadWorldKnowledge]
+ -[HPSSiriRestrictions allowsExplicitContent]
+ -[HPSSiriRestrictions allowsMathAssistance]
+ -[HPSSiriRestrictions allowsSafari]
+ -[HPSSiriRestrictions allowsWritingAssistance]
+ -[HPSSiriRestrictions description]
+ -[HPSSiriRestrictions encodeWithCoder:]
+ -[HPSSiriRestrictions initWithAllowsBroadWorldKnowledge:allowsWritingAssistance:allowsMathAssistance:reducesSensitiveContent:allowsExplicitContent:allowsSafari:limitsAdultWebsites:]
+ -[HPSSiriRestrictions initWithCoder:]
+ -[HPSSiriRestrictions limitsAdultWebsites]
+ -[HPSSiriRestrictions reducesSensitiveContent]
+ -[HPSSiriRestrictionsSession .cxx_destruct]
+ -[HPSSiriRestrictionsSession applySiriRestrictions:completionHandler:]
+ -[HPSSiriRestrictionsSession connection]
+ -[HPSSiriRestrictionsSession dealloc]
+ -[HPSSiriRestrictionsSession init]
+ -[HPSSiriRestrictionsSession setConnection:]
+ _HPSSiriRestrictionsConfigureXPCInterface
+ _OBJC_CLASS_$_HPSSiriRestrictions
+ _OBJC_CLASS_$_HPSSiriRestrictionsSession
+ _OBJC_IVAR_$_HPSSiriRestrictions._allowsBroadWorldKnowledge
+ _OBJC_IVAR_$_HPSSiriRestrictions._allowsExplicitContent
+ _OBJC_IVAR_$_HPSSiriRestrictions._allowsMathAssistance
+ _OBJC_IVAR_$_HPSSiriRestrictions._allowsSafari
+ _OBJC_IVAR_$_HPSSiriRestrictions._allowsWritingAssistance
+ _OBJC_IVAR_$_HPSSiriRestrictions._limitsAdultWebsites
+ _OBJC_IVAR_$_HPSSiriRestrictions._reducesSensitiveContent
+ _OBJC_IVAR_$_HPSSiriRestrictionsSession._connection
+ _OBJC_METACLASS_$_HPSSiriRestrictions
+ _OBJC_METACLASS_$_HPSSiriRestrictionsSession
+ __OBJC_$_CLASS_METHODS_HPSSiriRestrictions
+ __OBJC_$_CLASS_PROP_LIST_HPSSiriRestrictions
+ __OBJC_$_INSTANCE_METHODS_HPSSiriRestrictions
+ __OBJC_$_INSTANCE_METHODS_HPSSiriRestrictionsSession
+ __OBJC_$_INSTANCE_VARIABLES_HPSSiriRestrictions
+ __OBJC_$_INSTANCE_VARIABLES_HPSSiriRestrictionsSession
+ __OBJC_$_PROP_LIST_HPSSiriRestrictions
+ __OBJC_$_PROP_LIST_HPSSiriRestrictionsSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HPSSiriRestrictionsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HPSSiriRestrictionsProtocol
+ __OBJC_$_PROTOCOL_REFS_HPSSiriRestrictionsProtocol
+ __OBJC_CLASS_PROTOCOLS_$_HPSSiriRestrictions
+ __OBJC_CLASS_RO_$_HPSSiriRestrictions
+ __OBJC_CLASS_RO_$_HPSSiriRestrictionsSession
+ __OBJC_LABEL_PROTOCOL_$_HPSSiriRestrictionsProtocol
+ __OBJC_METACLASS_RO_$_HPSSiriRestrictions
+ __OBJC_METACLASS_RO_$_HPSSiriRestrictionsSession
+ __OBJC_PROTOCOL_$_HPSSiriRestrictionsProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_HPSSiriRestrictionsProtocol
+ ___70-[HPSSiriRestrictionsSession applySiriRestrictions:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_retainBlock
CStrings:
+ "<%@: worldKnowledge=%d writing=%d math=%d reduceSensitive=%d explicit=%d safari=%d limitAdult=%d>"
+ "allowsBroadWorldKnowledge"
+ "allowsExplicitContent"
+ "allowsMathAssistance"
+ "allowsSafari"
+ "allowsWritingAssistance"
+ "limitsAdultWebsites"
+ "reducesSensitiveContent"
```
