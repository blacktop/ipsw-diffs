## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-117.0.0.0.0
-  __TEXT.__text: 0x419f4
+138.1.0.0.0
+  __TEXT.__text: 0x42438
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x4440
-  __TEXT.__objc_methlist: 0x1c8c
+  __TEXT.__objc_stubs: 0x45e0
+  __TEXT.__objc_methlist: 0x1ce4
   __TEXT.__const: 0xe2
-  __TEXT.__objc_methname: 0x5d0a
-  __TEXT.__cstring: 0xaf4e
-  __TEXT.__oslogstring: 0x7393
+  __TEXT.__objc_methname: 0x5ec2
+  __TEXT.__cstring: 0xb11e
+  __TEXT.__oslogstring: 0x7495
   __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methtype: 0x30db
+  __TEXT.__objc_methtype: 0x3142
   __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__unwind_info: 0x548
+  __TEXT.__unwind_info: 0x558
   __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__cfstring: 0x1d80
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x2608
-  __DATA.__objc_selrefs: 0x1620
-  __DATA.__objc_ivar: 0x1f4
+  __DATA.__objc_const: 0x2670
+  __DATA.__objc_selrefs: 0x1688
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x590
   __DATA.__bss: 0x338

   - /System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B9907983-7298-3ED0-BA1F-83D11E73FF81
-  Functions: 606
-  Symbols:   369
-  CStrings:  3530
+  UUID: CE7D0FAD-7EC3-3608-B410-6C4F7BE409A2
+  Functions: 614
+  Symbols:   372
+  CStrings:  3566
 
Symbols:
+ _OBJC_CLASS_$_IDSFirewall
+ _OBJC_CLASS_$_IDSFirewallEntry
+ _OBJC_CLASS_$_IDSURI
CStrings:
+ "-[IDSSessionEmbeddedControllerBase addSessionToFirewall:]"
+ "-[IDSSessionEmbeddedControllerBase addSessionToFirewall:]_block_invoke"
+ "-[IDSSessionEmbeddedControllerBase removeSessionFromFirewall:]"
+ "-[IDSSessionEmbeddedControllerBase removeSessionFromFirewall:]_block_invoke"
+ "@\"IDSFirewall\""
+ "Added session to firewall"
+ "Failed to add session to the firewall, error is (%d) %s"
+ "Failed to remove session from the firewall, error is (%d) %s"
+ "Missing IDS Firewall"
+ "Removed session from firewall"
+ "T@\"IDSFirewall\",&,V_idsFirewall"
+ "TB,V_calledAddSessionToFirewall"
+ "URIWithPrefixedURI:"
+ "[%s:%d] Added session to firewall"
+ "[%s:%d] Failed to add session to the firewall, error is (%d) %s"
+ "[%s:%d] Failed to remove session from the firewall, error is (%d) %s"
+ "[%s:%d] Missing IDS Firewall"
+ "[%s:%d] Removed session from firewall"
+ "[%s:%d] idsFirewall  %p"
+ "_calledAddSessionToFirewall"
+ "_idsFirewall"
+ "addSessionToFirewall:"
+ "calledAddSessionToFirewall"
+ "donateEntries:withCompletion:"
+ "idsFirewall"
+ "idsFirewall  %p"
+ "initWithService:queue:"
+ "initWithURI:"
+ "removeDonatedEntries:withCompletion:"
+ "removeSessionFromFirewall:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "setCalledAddSessionToFirewall:"
+ "setIdsFirewall:"
+ "tokenFreeURI"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
