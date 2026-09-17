## SystemMigrationNetwork

> `/System/Library/PrivateFrameworks/SystemMigrationNetwork.framework/Versions/A/SystemMigrationNetwork`

```diff

-1428.0.3.0.0
-  __TEXT.__text: 0x3c914
-  __TEXT.__objc_methlist: 0x4598
+1439.0.0.0.0
+  __TEXT.__text: 0x3cf94
+  __TEXT.__objc_methlist: 0x4618
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x9863
-  __TEXT.__gcc_except_tab: 0xea4
+  __TEXT.__cstring: 0x98fd
+  __TEXT.__gcc_except_tab: 0xed0
   __TEXT.__ustring: 0x2cf8
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d0
+  __DATA_CONST.__objc_selrefs: 0x2a20
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xf0
-  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__got: 0x5c0
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x9880
-  __AUTH_CONST.__objc_const: 0x6878
+  __AUTH_CONST.__cfstring: 0x9940
+  __AUTH_CONST.__objc_const: 0x6938
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x11f8
-  __DATA.__objc_ivar: 0x534
+  __AUTH.__objc_data: 0x1248
+  __DATA.__objc_ivar: 0x538
   __DATA.__data: 0x318
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x28

   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1538
-  Symbols:   4066
-  CStrings:  1283
+  Functions: 1550
+  Symbols:   4103
+  CStrings:  1289
 
Symbols:
+ +[SMNDiscoveryMetrics recordPeerAppearance]
+ +[SMNDiscoveryMetrics recordPeerDisappearance]
+ +[SMNDiscoveryMetrics recordResolveAttempt]
+ +[SMNDiscoveryMetrics recordResolveRetry]
+ +[SMNDiscoveryMetrics recordResolveTimeout]
+ +[SMNDiscoveryMetrics recordSilentReject]
+ +[SMNDiscoveryMetrics snapshot]
+ -[SMNNetworkMigrationBrowser _recordSilentRejectOnceForPeer:]
+ -[SMNNetworkMigrationBrowser setSilentlyRejectedNames:]
+ -[SMNNetworkMigrationBrowser silentlyRejectedNames]
+ GCC_except_table14
+ OBJC_IVAR_$_SMNNetworkMigrationBrowser._silentlyRejectedNames
+ _OBJC_CLASS_$_SMNDiscoveryMetrics
+ _OBJC_METACLASS_$_SMNDiscoveryMetrics
+ __66-[SMNNetworkMigrationBrowser session:resolvedPeerNamed:txtRecord:]_block_invoke
+ __OBJC_$_CLASS_METHODS_SMNDiscoveryMetrics
+ __OBJC_CLASS_RO_$_SMNDiscoveryMetrics
+ __OBJC_METACLASS_RO_$_SMNDiscoveryMetrics
+ ___61-[SMNNetworkMigrationBrowser _recordSilentRejectOnceForPeer:]_block_invoke
+ _objc_msgSend$_recordSilentRejectOnceForPeer:
+ _objc_msgSend$recordPeerAppearance
+ _objc_msgSend$recordPeerDisappearance
+ _objc_msgSend$recordResolveAttempt
+ _objc_msgSend$recordResolveRetry
+ _objc_msgSend$recordResolveTimeout
+ _objc_msgSend$recordSilentReject
+ _objc_msgSend$setSilentlyRejectedNames:
+ _objc_msgSend$silentlyRejectedNames
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sLock
+ _sPeerAppearances
+ _sPeerDisappearances
+ _sResolveAttempts
+ _sResolveRetries
+ _sResolveTimeouts
+ _sSilentRejects
CStrings:
+ "DiscoveryPeerAppearances"
+ "DiscoveryPeerDisappearances"
+ "DiscoveryResolveAttempts"
+ "DiscoveryResolveRetries"
+ "DiscoveryResolveTimeouts"
+ "DiscoverySilentRejectCount"
```
