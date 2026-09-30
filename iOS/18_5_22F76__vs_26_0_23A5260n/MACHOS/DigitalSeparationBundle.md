## DigitalSeparationBundle

> `/System/Library/DigitalSeparation/SharingSources/DigitalSeparationBundle.bundle/DigitalSeparationBundle`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x58ac
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x704
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__objc_methname: 0x1382
+1323.0.6.0.1
+  __TEXT.__text: 0x5638
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__objc_methlist: 0x73c
+  __TEXT.__const: 0x20
+  __TEXT.__objc_methname: 0x1266
   __TEXT.__objc_classname: 0xf7
-  __TEXT.__objc_methtype: 0x578
-  __TEXT.__cstring: 0x31b
-  __TEXT.__oslogstring: 0x861
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x580
+  __TEXT.__objc_methtype: 0x5f4
+  __TEXT.__cstring: 0x2bb
+  __TEXT.__oslogstring: 0x8eb
+  __TEXT.__unwind_info: 0x180
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0xf40
-  __DATA.__objc_selrefs: 0x518
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_const: 0xf18
+  __DATA.__objc_selrefs: 0x4e0
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x300
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1EDDD994-B5F9-3D72-9021-FCF504FBC912
-  Functions: 116
-  Symbols:   102
-  CStrings:  376
+  UUID: 6FE0F84D-8140-344C-8D31-44CD2A3F8829
+  Functions: 108
+  Symbols:   95
+  CStrings:  361
 
Symbols:
+ _DSSourceErrorDomain
- _HMDSSourceHomeManagerRefreshTimeout
- __Unwind_Resume
- ___objc_personality_v0
- _objc_retain
- _objc_setProperty_atomic
- _objc_setProperty_atomic_copy
- _os_unfair_lock_lock_with_options
- _os_unfair_lock_unlock
CStrings:
+ "%{public}@Calling completion with DSSourceErroriCloudDisabled error because Home iCloud switch is disabled. Status: %@, DataSyncState: %@"
+ "%{public}@Failed to remove access code: %@"
+ "%{public}@Received did update homes callback"
+ "@\"HMDSContext\""
+ "@\"NAFuture\"16@0:8"
+ "@\"NAFuture\"24@0:8@\"HMHome\"16"
+ "@\"NAFuture\"24@0:8@\"HMHomeInvitation\"16"
+ "@\"NAFuture\"32@0:8@\"HMUser\"16@\"HMHome\"24"
+ "@\"NAFuture\"32@0:8@\"NSString\"16@\"HMHome\"24"
+ "T@\"HMDSContext\",R,V_context"
+ "T@\"NAFuture\",R"
+ "T@\"NAFuture\",R,V_didUpdateHomesFuture"
+ "T@\"NSArray\",R,C"
+ "_context"
+ "_performBlock:"
+ "context"
+ "digital.separation.context"
+ "digital.separation.source"
+ "initWithContext:"
+ "refreshData"
- "%{public}@Failed to remove access code"
- "%{public}@did update homes for DigitalSeparation"
- "@\"HMDSContext\"16@?0@\"HMHomeManager\"8"
- "@\"NAFuture\"16@?0@\"NSNull\"8"
- "@\"NAFuture\"8@?0"
- "@?"
- "@?16@0:8"
- "DigitalSeparation API Call"
- "Q"
- "T@\"NAFuture\",&,V_apiCallFuture"
- "T@\"NAFuture\",&,V_didUpdateHomesFuture"
- "T@\"NSArray\",R,C,V_homes"
- "T@?,C,V_contextFactory"
- "TQ,R,V_dataSyncState"
- "TQ,R,V_status"
- "_apiCallFuture"
- "_beginActiveAssertionWithReason:"
- "_contextFactory"
- "_dataSyncState"
- "_endActiveAssertion:"
- "_flatMapWithAssertion:"
- "_homes"
- "_lock"
- "_status"
- "apiCallFuture"
- "contextFactory"
- "digital.separation.home"
- "initWithHomeManager:homes:"
- "initWithHomes:"
- "isCurrentUser"
- "setApiCallFuture:"
- "setContextFactory:"
- "setDidUpdateHomesFuture:"
- "v16@?0@\"NSError\"8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
