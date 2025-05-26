## DADaemonSupport

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`

```diff

-2653.0.0.0.0
-  __TEXT.__text: 0x371b0
+2653.1.1.4.0
+  __TEXT.__text: 0x36e04
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x20d4
+  __TEXT.__objc_methlist: 0x20dc
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__oslogstring: 0x62a0
-  __TEXT.__cstring: 0x13ef
-  __TEXT.__unwind_info: 0xaec
+  __TEXT.__gcc_except_tab: 0x62c
+  __TEXT.__oslogstring: 0x6306
+  __TEXT.__cstring: 0x13a8
+  __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_classname: 0x6f6
-  __TEXT.__objc_methname: 0x7e7d
+  __TEXT.__objc_methname: 0x7d95
   __TEXT.__objc_methtype: 0x1204
-  __TEXT.__objc_stubs: 0x6aa0
-  __DATA_CONST.__got: 0x7c0
+  __TEXT.__objc_stubs: 0x6a20
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5570
-  __DATA_CONST.__objc_selrefs: 0x1e60
+  __DATA_CONST.__objc_selrefs: 0x1e40
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__objc_const: 0xc58
-  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6b0
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_classrefs: 0x378
+  __DATA.__objc_classrefs: 0x370
   __DATA.__objc_superrefs: 0xd8
   __DATA.__objc_ivar: 0x284
   __DATA.__data: 0x8b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 900
-  Symbols:   3922
-  CStrings:  2020
+  Functions: 899
+  Symbols:   3919
+  CStrings:  2014
 
Symbols:
+ -[DADAgentManager releaseAgents]
+ -[DADMain _boostConnectedActivityPriority]
+ -[DADMain _evaluateConnectedStartupActivityStatus]
+ -[DADMain boostConnectedActivityPriority]
+ GCC_except_table16
+ GCC_except_table36
+ GCC_except_table45
+ GCC_except_table68
+ _XPC_ACTIVITY_REQUIRES_BUDDY_COMPLETE
+ _XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL
+ _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
+ ___29-[DADAgentManager loadAgents]_block_invoke.36
+ ___32-[DADAgentManager releaseAgents]_block_invoke
+ ___48-[DADAgentManager _loadAndStartMonitoringAgents]_block_invoke.69
+ ___50-[DADMain _evaluateConnectedStartupActivityStatus]_block_invoke
+ ___block_literal_global.119
+ ___block_literal_global.29
+ ___block_literal_global.59
+ ___block_literal_global.62
+ ___block_literal_global.72
+ __boostConnectedPriority
+ __connectedLock
+ _objc_msgSend$_boostConnectedActivityPriority
+ _objc_msgSend$_evaluateConnectedStartupActivityStatus
+ _objc_msgSend$boostConnectedActivityPriority
+ _objc_msgSend$releaseAgents
- -[DADAgentManager _accountInfoPath]
- -[DADAgentManager saveAndReleaseAgents]
- -[DADMain evaluateConnectedStartupActivityStatus]
- GCC_except_table17
- GCC_except_table37
- GCC_except_table46
- GCC_except_table69
- _OBJC_CLASS_$_MCProfileConnection
- ___22-[DADMain xpc_checkin]_block_invoke.76
- ___24-[DADMain agentsStarted]_block_invoke
- ___29-[DADAgentManager loadAgents]_block_invoke.40
- ___39-[DADAgentManager saveAndReleaseAgents]_block_invoke
- ___48-[DADAgentManager _loadAndStartMonitoringAgents]_block_invoke.84
- ___49-[DADMain evaluateConnectedStartupActivityStatus]_block_invoke
- ___block_literal_global.130
- ___block_literal_global.32
- ___block_literal_global.74
- ___block_literal_global.77
- ___block_literal_global.87
- _kDAAccountPersistentUUID
- _objc_msgSend$_accountInfoPath
- _objc_msgSend$applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:
- _objc_msgSend$evaluateConnectedStartupActivityStatus
- _objc_msgSend$initWithContentsOfFile:
- _objc_msgSend$removeOrphanedClientRestrictionsWithCompletion:
- _objc_msgSend$saveAndReleaseAgents
- _objc_msgSend$sharedConnection
- _objc_msgSend$writeToFile:atomically:
CStrings:
+ "Connected activity hasn't been created yet; can't boost priority yet."
+ "Requesting connected activity run with priority utility"
+ "Requesting expedited handling of connected activity"
+ "_boostConnectedActivityPriority"
+ "_evaluateConnectedStartupActivityStatus"
+ "boostConnectedActivityPriority"
+ "releaseAgents"
- "AccountInformation.plist"
- "DAAgentClass"
- "Error when cleaning up client restrictions for persistentUUID %@.  Error %@"
- "Identifier"
- "_accountInfoPath"
- "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
- "com.apple.eas.account"
- "evaluateConnectedStartupActivityStatus"
- "initWithContentsOfFile:"
- "removeOrphanedClientRestrictionsWithCompletion:"
- "saveAndReleaseAgents"
- "sharedConnection"
- "writeToFile:atomically:"

```
