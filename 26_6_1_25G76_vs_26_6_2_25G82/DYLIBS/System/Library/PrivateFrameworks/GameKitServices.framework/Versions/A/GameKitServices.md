## GameKitServices

> `/System/Library/PrivateFrameworks/GameKitServices.framework/Versions/A/GameKitServices`

```diff

 2215.5.1.0.0
-  __TEXT.__text: 0x7adb0
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x2ea8
+  __TEXT.__text: 0x7bb64
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0x2f40
   __TEXT.__const: 0x1960
-  __TEXT.__gcc_except_tab: 0x95c
-  __TEXT.__cstring: 0x697c
-  __TEXT.__oslogstring: 0x11be3
-  __TEXT.__unwind_info: 0xfe0
-  __TEXT.__objc_classname: 0x459
-  __TEXT.__objc_methname: 0x6cb9
+  __TEXT.__gcc_except_tab: 0x8a0
+  __TEXT.__cstring: 0x69ae
+  __TEXT.__oslogstring: 0x11efd
+  __TEXT.__unwind_info: 0x1008
+  __TEXT.__objc_classname: 0x476
+  __TEXT.__objc_methname: 0x6e01
   __TEXT.__objc_methtype: 0x19a5
-  __TEXT.__objc_stubs: 0x5380
+  __TEXT.__objc_stubs: 0x5500
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ba0
+  __DATA_CONST.__objc_selrefs: 0x1bf8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x908
-  __AUTH_CONST.__const: 0xb60
+  __AUTH_CONST.__auth_got: 0x910
+  __AUTH_CONST.__const: 0xb80
   __AUTH_CONST.__cfstring: 0x1f80
-  __AUTH_CONST.__objc_const: 0x4d30
+  __AUTH_CONST.__objc_const: 0x4e80
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_ivar: 0x4f4
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0x638
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xb40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1633
-  Symbols:   3171
-  CStrings:  3424
+  Functions: 1655
+  Symbols:   3210
+  CStrings:  3452
 
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
+ OBJC_IVAR_$_GKDiscoveryBonjour._txtLookupContexts
+ OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._callback
+ OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._owner
+ OBJC_IVAR_$_GKDiscoveryBonjourTxtContext._serviceRef
+ _OBJC_CLASS_$_GKDiscoveryBonjourTxtContext
+ _OBJC_METACLASS_$_GKDiscoveryBonjourTxtContext
+ __OBJC_$_INSTANCE_METHODS_GKDiscoveryBonjourTxtContext
+ __OBJC_$_INSTANCE_VARIABLES_GKDiscoveryBonjourTxtContext
+ __OBJC_$_PROP_LIST_GKDiscoveryBonjourTxtContext
+ __OBJC_CLASS_RO_$_GKDiscoveryBonjourTxtContext
+ __OBJC_METACLASS_RO_$_GKDiscoveryBonjourTxtContext
+ ___57+[GKVoiceChatDictionary expectedActualDictionaryKeyTypes]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_57_e8_32o40o_e22_v16?0"NSDictionary"8l
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
+ expectedActualDictionaryKeyTypes.expectedKeyTypes
+ expectedActualDictionaryKeyTypes.once
- GCC_except_table13
- ___block_descriptor_57_e8_32o40r_e22_v16?0"NSDictionary"8l
CStrings:
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: packet iLen=%d exceeds dest capacity=%d; dropping"
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
