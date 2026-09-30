## AppleDeviceQuerySupport

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`

```diff

-340.120.3.0.0
-  __TEXT.__text: 0xadfc
+392.0.0.0.0
+  __TEXT.__text: 0xafac
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x458
+  __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__cstring: 0x464b
+  __TEXT.__cstring: 0x4518
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0x12b
-  __TEXT.__objc_methname: 0xf55
-  __TEXT.__objc_methtype: 0x2f1
-  __TEXT.__objc_stubs: 0x11e0
+  __TEXT.__objc_classname: 0xbf
+  __TEXT.__objc_methname: 0xf8f
+  __TEXT.__objc_methtype: 0x2ea
+  __TEXT.__objc_stubs: 0x1220
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x708
+  __AUTH_CONST.__objc_const: 0x718
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0xb40
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF899D9C-FA86-301D-92E7-8B0C249DD622
-  Functions: 175
-  Symbols:   811
-  CStrings:  1154
+  UUID: DC47ED22-C6A0-375A-8CAF-6889C43FC8D1
+  Functions: 179
+  Symbols:   823
+  CStrings:  1159
 
Symbols:
+ +[ZhuGeInternalSupportAssistant armoryClassName]
+ +[ZhuGeInternalSupportAssistant cacheList]
+ +[ZhuGeInternalSupportAssistant classList]
+ +[ZhuGeInternalSupportAssistant dylibHandler]
+ +[ZhuGeInternalSupportAssistant executeCacheRefresh]
+ +[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]
+ +[ZhuGeInternalSupportAssistant getInternalSupportPath]
+ +[ZhuGeInternalSupportAssistant getXpcProxyWithError:]
+ +[ZhuGeInternalSupportAssistant isInternalAssistant]
+ +[ZhuGeInternalSupportAssistant isXpcConnectionValid]
+ +[ZhuGeInternalSupportAssistant isXpcConnectionValid].cold.1
+ +[ZhuGeInternalSupportAssistant recursiveMutex]
+ +[ZhuGeInternalSupportAssistant recursiveMutex].cold.1
+ +[ZhuGeInternalSupportAssistant registerCacheRefresh:]
+ +[ZhuGeInternalSupportAssistant serviceXpcName]
+ +[ZhuGeInternalSupportAssistant setCacheList:]
+ +[ZhuGeInternalSupportAssistant setDylibHandler:]
+ +[ZhuGeInternalSupportAssistant setIsXpcConnectionValid:]
+ +[ZhuGeInternalSupportAssistant setXpcConnection:]
+ +[ZhuGeInternalSupportAssistant xpcConnection]
+ +[ZhuGeSingleton accessInstanceVariablesDirectly]
+ +[ZhuGeSingleton sharedInstance]
+ +[ZhuGeSingleton sharedInstance].cold.1
+ +[ZhuGeSupportAssistant armoryClassName]
+ +[ZhuGeSupportAssistant classList]
+ +[ZhuGeSupportAssistant getDylibHandlerWithError:]
+ +[ZhuGeSupportAssistant getDylibHandlerWithError:].cold.1
+ +[ZhuGeSupportAssistant getSharedInstanceByName:withError:]
+ +[ZhuGeSupportAssistant getXpcProxyWithError:]
+ +[ZhuGeSupportAssistant getXpcProxyWithError:].cold.1
+ +[ZhuGeSupportAssistant isInternalAssistant]
+ +[ZhuGeSupportAssistant isKey:withError:]
+ +[ZhuGeSupportAssistant serviceXpcName]
+ -[ZhuGeCache .cxx_destruct]
+ -[ZhuGeCache cacheDict]
+ -[ZhuGeCache cacheList]
+ -[ZhuGeCache cacheType]
+ -[ZhuGeCache capacity]
+ -[ZhuGeCache clearCache]
+ -[ZhuGeCache delCacheForKey:]
+ -[ZhuGeCache getCacheForKey:]
+ -[ZhuGeCache initWithName:andCapacity:andCacheType:]
+ -[ZhuGeCache name]
+ -[ZhuGeCache setCache:forKey:withError:]
+ -[ZhuGeLocker .cxx_destruct]
+ -[ZhuGeLocker initData]
+ -[ZhuGeLocker keysCacheForCopyValue]
+ -[ZhuGeLocker logHandler]
+ -[ZhuGeLocker setKeysCacheForCopyValue:]
+ -[ZhuGeLocker setLogHandler:]
+ -[ZhuGeRestoreLog printRemoteLog:]
+ -[ZhuGeSingleton initData]
+ _OBJC_CLASS_$_ZhuGeCache
+ _OBJC_CLASS_$_ZhuGeInternalSupportAssistant
+ _OBJC_CLASS_$_ZhuGeLocker
+ _OBJC_CLASS_$_ZhuGeRestoreLog
+ _OBJC_CLASS_$_ZhuGeSingleton
+ _OBJC_CLASS_$_ZhuGeSupportAssistant
+ _OBJC_IVAR_$_ZhuGeCache._cacheDict
+ _OBJC_IVAR_$_ZhuGeCache._cacheList
+ _OBJC_IVAR_$_ZhuGeCache._cacheType
+ _OBJC_IVAR_$_ZhuGeCache._capacity
+ _OBJC_IVAR_$_ZhuGeCache._name
+ _OBJC_IVAR_$_ZhuGeCache.aRecursiveMutex
+ _OBJC_IVAR_$_ZhuGeLocker._keysCacheForCopyValue
+ _OBJC_IVAR_$_ZhuGeLocker._logHandler
+ _OBJC_IVAR_$_ZhuGeLocker.recursiveMutexForCopyValue
+ _OBJC_METACLASS_$_ZhuGeCache
+ _OBJC_METACLASS_$_ZhuGeInternalSupportAssistant
+ _OBJC_METACLASS_$_ZhuGeLocker
+ _OBJC_METACLASS_$_ZhuGeRestoreLog
+ _OBJC_METACLASS_$_ZhuGeSingleton
+ _OBJC_METACLASS_$_ZhuGeSupportAssistant
+ __OBJC_$_CLASS_METHODS_ZhuGeInternalSupportAssistant
+ __OBJC_$_CLASS_METHODS_ZhuGeSingleton
+ __OBJC_$_CLASS_METHODS_ZhuGeSupportAssistant
+ __OBJC_$_CLASS_PROP_LIST_ZhuGeInternalSupportAssistant
+ __OBJC_$_INSTANCE_METHODS_ZhuGeCache
+ __OBJC_$_INSTANCE_METHODS_ZhuGeLocker
+ __OBJC_$_INSTANCE_METHODS_ZhuGeRestoreLog
+ __OBJC_$_INSTANCE_METHODS_ZhuGeSingleton
+ __OBJC_$_INSTANCE_VARIABLES_ZhuGeCache
+ __OBJC_$_INSTANCE_VARIABLES_ZhuGeLocker
+ __OBJC_$_PROP_LIST_ZhuGeCache
+ __OBJC_$_PROP_LIST_ZhuGeLocker
+ __OBJC_CLASS_PROTOCOLS_$_ZhuGeRestoreLog
+ __OBJC_CLASS_RO_$_ZhuGeCache
+ __OBJC_CLASS_RO_$_ZhuGeInternalSupportAssistant
+ __OBJC_CLASS_RO_$_ZhuGeLocker
+ __OBJC_CLASS_RO_$_ZhuGeRestoreLog
+ __OBJC_CLASS_RO_$_ZhuGeSingleton
+ __OBJC_CLASS_RO_$_ZhuGeSupportAssistant
+ __OBJC_METACLASS_RO_$_ZhuGeCache
+ __OBJC_METACLASS_RO_$_ZhuGeInternalSupportAssistant
+ __OBJC_METACLASS_RO_$_ZhuGeLocker
+ __OBJC_METACLASS_RO_$_ZhuGeRestoreLog
+ __OBJC_METACLASS_RO_$_ZhuGeSingleton
+ __OBJC_METACLASS_RO_$_ZhuGeSupportAssistant
+ ___32+[ZhuGeSingleton sharedInstance]_block_invoke
+ ___46+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke
+ ___46+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2
+ ___46+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3
+ ___46+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4
+ ___47+[ZhuGeInternalSupportAssistant recursiveMutex]_block_invoke
+ ___50+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke
+ ___53+[ZhuGeInternalSupportAssistant isXpcConnectionValid]_block_invoke
+ ___54+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke
+ ___54+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2
+ ___54+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3
+ ___block_literal_global.2
+ __isXpcConnectionValid
+ __xpcConnection
+ _getXpcProxyWithError:.aConnection
+ _getXpcProxyWithError:.isConnectionValid
+ _isXpcConnectionValid.aToken
+ _objc_msgSend$isXpcConnectionValid
+ _objc_msgSend$setIsXpcConnectionValid:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$xpcConnection
- +[AppleDeviceQueryInternalSupportAssistantSupport armoryClassName]
- +[AppleDeviceQueryInternalSupportAssistantSupport cacheList]
- +[AppleDeviceQueryInternalSupportAssistantSupport classList]
- +[AppleDeviceQueryInternalSupportAssistantSupport dylibHandler]
- +[AppleDeviceQueryInternalSupportAssistantSupport executeCacheRefresh]
- +[AppleDeviceQueryInternalSupportAssistantSupport getDylibHandlerWithError:]
- +[AppleDeviceQueryInternalSupportAssistantSupport getInternalSupportPath]
- +[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]
- +[AppleDeviceQueryInternalSupportAssistantSupport isInternalAssistant]
- +[AppleDeviceQueryInternalSupportAssistantSupport recursiveMutex]
- +[AppleDeviceQueryInternalSupportAssistantSupport recursiveMutex].cold.1
- +[AppleDeviceQueryInternalSupportAssistantSupport registerCacheRefresh:]
- +[AppleDeviceQueryInternalSupportAssistantSupport serviceXpcName]
- +[AppleDeviceQueryInternalSupportAssistantSupport setCacheList:]
- +[AppleDeviceQueryInternalSupportAssistantSupport setDylibHandler:]
- +[AppleDeviceQueryInternalSupportAssistantSupport setXpcProxy:]
- +[AppleDeviceQueryInternalSupportAssistantSupport xpcProxy]
- +[AppleDeviceQuerySingletonSupport accessInstanceVariablesDirectly]
- +[AppleDeviceQuerySingletonSupport sharedInstance]
- +[AppleDeviceQuerySingletonSupport sharedInstance].cold.1
- +[AppleDeviceQuerySupportAssistantSupport armoryClassName]
- +[AppleDeviceQuerySupportAssistantSupport classList]
- +[AppleDeviceQuerySupportAssistantSupport getDylibHandlerWithError:]
- +[AppleDeviceQuerySupportAssistantSupport getDylibHandlerWithError:].cold.1
- +[AppleDeviceQuerySupportAssistantSupport getSharedInstanceByName:withError:]
- +[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]
- +[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:].cold.1
- +[AppleDeviceQuerySupportAssistantSupport isInternalAssistant]
- +[AppleDeviceQuerySupportAssistantSupport isKey:withError:]
- +[AppleDeviceQuerySupportAssistantSupport serviceXpcName]
- -[AppleDeviceQueryCacheSupport .cxx_destruct]
- -[AppleDeviceQueryCacheSupport cacheDict]
- -[AppleDeviceQueryCacheSupport cacheList]
- -[AppleDeviceQueryCacheSupport cacheType]
- -[AppleDeviceQueryCacheSupport capacity]
- -[AppleDeviceQueryCacheSupport clearCache]
- -[AppleDeviceQueryCacheSupport delCacheForKey:]
- -[AppleDeviceQueryCacheSupport getCacheForKey:]
- -[AppleDeviceQueryCacheSupport initWithName:andCapacity:andCacheType:]
- -[AppleDeviceQueryCacheSupport name]
- -[AppleDeviceQueryCacheSupport setCache:forKey:withError:]
- -[AppleDeviceQueryLockerSupport .cxx_destruct]
- -[AppleDeviceQueryLockerSupport initData]
- -[AppleDeviceQueryLockerSupport keysCacheForCopyValue]
- -[AppleDeviceQueryLockerSupport logHandler]
- -[AppleDeviceQueryLockerSupport setKeysCacheForCopyValue:]
- -[AppleDeviceQueryLockerSupport setLogHandler:]
- -[AppleDeviceQueryRestoreLogSupport printRemoteLog:]
- -[AppleDeviceQuerySingletonSupport initData]
- _OBJC_CLASS_$_AppleDeviceQueryCacheSupport
- _OBJC_CLASS_$_AppleDeviceQueryInternalSupportAssistantSupport
- _OBJC_CLASS_$_AppleDeviceQueryLockerSupport
- _OBJC_CLASS_$_AppleDeviceQueryRestoreLogSupport
- _OBJC_CLASS_$_AppleDeviceQuerySingletonSupport
- _OBJC_CLASS_$_AppleDeviceQuerySupportAssistantSupport
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport._cacheDict
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport._cacheList
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport._cacheType
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport._capacity
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport._name
- _OBJC_IVAR_$_AppleDeviceQueryCacheSupport.aRecursiveMutex
- _OBJC_IVAR_$_AppleDeviceQueryLockerSupport._keysCacheForCopyValue
- _OBJC_IVAR_$_AppleDeviceQueryLockerSupport._logHandler
- _OBJC_IVAR_$_AppleDeviceQueryLockerSupport.recursiveMutexForCopyValue
- _OBJC_METACLASS_$_AppleDeviceQueryCacheSupport
- _OBJC_METACLASS_$_AppleDeviceQueryInternalSupportAssistantSupport
- _OBJC_METACLASS_$_AppleDeviceQueryLockerSupport
- _OBJC_METACLASS_$_AppleDeviceQueryRestoreLogSupport
- _OBJC_METACLASS_$_AppleDeviceQuerySingletonSupport
- _OBJC_METACLASS_$_AppleDeviceQuerySupportAssistantSupport
- __OBJC_$_CLASS_METHODS_AppleDeviceQueryInternalSupportAssistantSupport
- __OBJC_$_CLASS_METHODS_AppleDeviceQuerySingletonSupport
- __OBJC_$_CLASS_METHODS_AppleDeviceQuerySupportAssistantSupport
- __OBJC_$_CLASS_PROP_LIST_AppleDeviceQueryInternalSupportAssistantSupport
- __OBJC_$_INSTANCE_METHODS_AppleDeviceQueryCacheSupport
- __OBJC_$_INSTANCE_METHODS_AppleDeviceQueryLockerSupport
- __OBJC_$_INSTANCE_METHODS_AppleDeviceQueryRestoreLogSupport
- __OBJC_$_INSTANCE_METHODS_AppleDeviceQuerySingletonSupport
- __OBJC_$_INSTANCE_VARIABLES_AppleDeviceQueryCacheSupport
- __OBJC_$_INSTANCE_VARIABLES_AppleDeviceQueryLockerSupport
- __OBJC_$_PROP_LIST_AppleDeviceQueryCacheSupport
- __OBJC_$_PROP_LIST_AppleDeviceQueryLockerSupport
- __OBJC_CLASS_PROTOCOLS_$_AppleDeviceQueryRestoreLogSupport
- __OBJC_CLASS_RO_$_AppleDeviceQueryCacheSupport
- __OBJC_CLASS_RO_$_AppleDeviceQueryInternalSupportAssistantSupport
- __OBJC_CLASS_RO_$_AppleDeviceQueryLockerSupport
- __OBJC_CLASS_RO_$_AppleDeviceQueryRestoreLogSupport
- __OBJC_CLASS_RO_$_AppleDeviceQuerySingletonSupport
- __OBJC_CLASS_RO_$_AppleDeviceQuerySupportAssistantSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQueryCacheSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQueryInternalSupportAssistantSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQueryLockerSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQueryRestoreLogSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQuerySingletonSupport
- __OBJC_METACLASS_RO_$_AppleDeviceQuerySupportAssistantSupport
- ___50+[AppleDeviceQuerySingletonSupport sharedInstance]_block_invoke
- ___64+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke
- ___64+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_2
- ___64+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_3
- ___64+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_4
- ___65+[AppleDeviceQueryInternalSupportAssistantSupport recursiveMutex]_block_invoke
- ___68+[AppleDeviceQuerySupportAssistantSupport getDylibHandlerWithError:]_block_invoke
- ___72+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke
- ___72+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke_2
- ___72+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke_3
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_literal_global.34
- ___block_literal_global.81
- __xpcProxy
- _getXpcProxyWithError:.aProxy
- _objc_msgSend$setXpcProxy:
- _objc_msgSend$xpcProxy
CStrings:
+ "%@ failed to provide a proxy with error : %@!"
+ "(null)"
+ "+[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]"
+ "+[ZhuGeInternalSupportAssistant getInternalSupportPath]"
+ "+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]"
+ "+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke"
+ "+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2"
+ "+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3"
+ "+[ZhuGeSupportAssistant getDylibHandlerWithError:]"
+ "+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke"
+ "+[ZhuGeSupportAssistant getSharedInstanceByName:withError:]"
+ "+[ZhuGeSupportAssistant getXpcProxyWithError:]"
+ "+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2"
+ "+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3"
+ "+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4"
+ "+[ZhuGeSupportAssistant isKey:withError:]"
+ "-[ZhuGeCache setCache:forKey:withError:]"
+ "/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib"
+ "@\"ZhuGeCache\""
+ "Failed to dlopen ZhuGe armory dylib with error: %s!"
+ "Failed to dlopen ZhuGe internal armory dylib with error: %s!"
+ "Failed to find class symbol for \"%@\" with error: %s!"
+ "Internal XPC connection is already available"
+ "OBJC_CLASS_$_ZhuGeArmory"
+ "OBJC_CLASS_$_ZhuGeLockerArmory"
+ "T@\"NSXPCConnection\",&"
+ "T@\"ZhuGeCache\",&,V_keysCacheForCopyValue"
+ "TB"
+ "XPC connection is already available"
+ "ZhuGe-392"
+ "ZhuGeCache"
+ "ZhuGeInternalSupportAssistant"
+ "ZhuGeLocker"
+ "ZhuGeRestoreLog"
+ "ZhuGeSingleton"
+ "ZhuGeSupport"
+ "ZhuGeSupportAssistant"
+ "isXpcConnectionValid"
+ "setIsXpcConnectionValid:"
+ "setXpcConnection:"
+ "v20@0:8B16"
+ "xpcConnection"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getDylibHandlerWithError:]"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getInternalSupportPath]"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke_2"
- "+[AppleDeviceQueryInternalSupportAssistantSupport getXpcProxyWithError:]_block_invoke_3"
- "+[AppleDeviceQuerySupportAssistantSupport getDylibHandlerWithError:]"
- "+[AppleDeviceQuerySupportAssistantSupport getDylibHandlerWithError:]_block_invoke"
- "+[AppleDeviceQuerySupportAssistantSupport getSharedInstanceByName:withError:]"
- "+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]"
- "+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_2"
- "+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_3"
- "+[AppleDeviceQuerySupportAssistantSupport getXpcProxyWithError:]_block_invoke_4"
- "+[AppleDeviceQuerySupportAssistantSupport isKey:withError:]"
- "-[AppleDeviceQueryCacheSupport setCache:forKey:withError:]"
- "/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib"
- "@\"AppleDeviceQueryCacheSupport\""
- "AppleDeviceQueryCacheSupport"
- "AppleDeviceQueryInternalSupportAssistantSupport"
- "AppleDeviceQueryLockerSupport"
- "AppleDeviceQueryRestoreLogSupport"
- "AppleDeviceQuerySingletonSupport"
- "AppleDeviceQuerySupport"
- "AppleDeviceQuerySupportAssistantSupport"
- "Connection failed to provide a synchronized proxy, error : %@!"
- "Failed to dlopen ZhuGe armory dylib!"
- "Failed to dlopen ZhuGe internal armory dylib!"
- "Failed to find class symbol for \"%@\"!"
- "Internal connection failed to provide a synchronized proxy, error : %@!"
- "OBJC_CLASS_$_AppleDeviceQueryArmory"
- "OBJC_CLASS_$_AppleDeviceQueryLockerArmory"
- "T@\"AppleDeviceQueryCacheSupport\",&,V_keysCacheForCopyValue"
- "T@,&"
- "XPC proxy is already available"
- "ZhuGe-340.120.3"
- "setXpcProxy:"
- "xpcProxy"

```
