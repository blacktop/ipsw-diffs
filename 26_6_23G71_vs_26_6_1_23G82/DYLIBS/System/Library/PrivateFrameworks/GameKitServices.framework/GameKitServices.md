## GameKitServices

> `/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices`

```diff

 2215.5.1.0.0
-  __TEXT.__text: 0x7b048
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x2ed8
+  __TEXT.__text: 0x7bdd4
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_methlist: 0x2f70
   __TEXT.__const: 0x1958
-  __TEXT.__gcc_except_tab: 0x978
-  __TEXT.__cstring: 0x6a7d
-  __TEXT.__oslogstring: 0x118e9
-  __TEXT.__unwind_info: 0xfe8
-  __TEXT.__objc_classname: 0x476
-  __TEXT.__objc_methname: 0x6d84
+  __TEXT.__gcc_except_tab: 0x8bc
+  __TEXT.__cstring: 0x6aaf
+  __TEXT.__oslogstring: 0x11bdd
+  __TEXT.__unwind_info: 0x1010
+  __TEXT.__objc_classname: 0x493
+  __TEXT.__objc_methname: 0x6ecc
   __TEXT.__objc_methtype: 0x19b0
-  __TEXT.__objc_stubs: 0x5500
+  __TEXT.__objc_stubs: 0x5680
   __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0xa58
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__const: 0xa30
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1c50
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x9c0
-  __AUTH_CONST.__const: 0x190
+  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x4d70
+  __AUTH_CONST.__objc_const: 0x4ec0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_ivar: 0x4f4
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0x638
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xc0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xb40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1616
-  Symbols:   3124
-  CStrings:  3461
+  Functions: 1637
+  Symbols:   3162
+  CStrings:  3489
 
Symbols:
+ +[GKVoiceChatDictionary expectedActualDictionaryKeyTypes]
+ +[GKVoiceChatDictionary isValidActualDictionary:]
+ -[GKDiscoveryBonjour _cancelAllTxtLookups]
+ -[GKDiscoveryBonjour _trackTxtLookupContext:]
+ -[GKDiscoveryBonjour _untrackTxtLookupContext:]
+ -[GKDiscoveryBonjourTxtContext callback]
+ -[GKDiscoveryBonjourTxtContext dealloc]
+ -[GKDiscoveryBonjourTxtContext owner]
+ -[GKDiscoveryBonjourTxtContext serviceRef]
+ -[GKDiscoveryBonjourTxtContext setCallback:]
+ -[GKDiscoveryBonjourTxtContext setOwner:]
+ -[GKDiscoveryBonjourTxtContext setServiceRef:]
+ _OBJC_CLASS_$_GKDiscoveryBonjourTxtContext
+ _OBJC_IVAR_$_GKDiscoveryBonjour._txtLookupContexts
+ _OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._callback
+ _OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._owner
+ _OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._serviceRef
+ _OBJC_METACLASS_$_GKDiscoveryBonjourTxtContext
+ __OBJC_$_INSTANCE_METHODS_GKDiscoveryBonjourTxtContext
+ __OBJC_$_INSTANCE_VARIABLES_GKDiscoveryBonjourTxtContext
+ __OBJC_$_PROP_LIST_GKDiscoveryBonjourTxtContext
+ __OBJC_CLASS_RO_$_GKDiscoveryBonjourTxtContext
+ __OBJC_METACLASS_RO_$_GKDiscoveryBonjourTxtContext
+ ___57+[GKVoiceChatDictionary expectedActualDictionaryKeyTypes]_block_invoke
+ ___block_descriptor_57_e8_32o40o_e22_v16?0"NSDictionary"8ls32l8s40l8
+ _expectedActualDictionaryKeyTypes.expectedKeyTypes
+ _expectedActualDictionaryKeyTypes.once
+ _objc_msgSend$_cancelAllTxtLookups
+ _objc_msgSend$_trackTxtLookupContext:
+ _objc_msgSend$_untrackTxtLookupContext:
+ _objc_msgSend$callback
+ _objc_msgSend$expectedActualDictionaryKeyTypes
+ _objc_msgSend$isValidActualDictionary:
+ _objc_msgSend$owner
+ _objc_msgSend$resolveTimeoutHandler
+ _objc_msgSend$serviceRef
+ _objc_msgSend$setCallback:
+ _objc_msgSend$setOwner:
+ _objc_msgSend$setServiceRef:
+ _objc_setProperty_atomic_copy
- ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_57_e8_32o40r_e22_v16?0"NSDictionary"8lr40l8s32l8
CStrings:
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: packet iLen=%d exceeds dest capacity=%d; dropping"
+ " [%s] %s:%d Failed to mutableCopy decoded actualDictionary"
+ " [%s] %s:%d GKVoiceChatDictionary decoded actualDictionary failed key/value validation"
+ " [%s] %s:%d GKVoiceChatDictionary decoded actualDictionary is not an NSDictionary"
+ " [%s] %s:%d GKVoiceChatDictionary key is not an NSString"
+ " [%s] %s:%d GKVoiceChatDictionary unknown key %s"
+ " [%s] %s:%d GKVoiceChatDictionary value for key %s has unexpected type"
+ " [%s] %s:%d parseConnectedPeers got non-array plist"
+ " [%s] %s:%d parseConnectedPeers got oversize array count=%lu max=%d"
+ "+[GKVoiceChatDictionary isValidActualDictionary:]"
+ "GKDiscoveryBonjourTxtContext"
+ "T@\"GKDiscoveryBonjour\",N,V_owner"
+ "T@?,C,N,V_callback"
+ "T@?,C,V_resolveTimeoutHandler"
+ "T^{_DNSServiceRef_t=},N,V_serviceRef"
+ "_callback"
+ "_cancelAllTxtLookups"
+ "_owner"
+ "_serviceRef"
+ "_trackTxtLookupContext:"
+ "_txtLookupContexts"
+ "_untrackTxtLookupContext:"
+ "expectedActualDictionaryKeyTypes"
+ "isValidActualDictionary:"
+ "owner"
+ "serviceRef"
+ "setCallback:"
+ "setOwner:"
+ "setServiceRef:"
- "T@?,C,N,V_resolveTimeoutHandler"
```
