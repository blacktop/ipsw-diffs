## AssertionServices

> `/System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices`

```diff

-945.80.1.0.1
-  __TEXT.__text: 0x7e24
+961.100.17.0.0
+  __TEXT.__text: 0x80c8
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x6fc
-  __TEXT.__const: 0x124
+  __TEXT.__objc_methlist: 0x898
+  __TEXT.__const: 0x11c
   __TEXT.__cstring: 0x88f
   __TEXT.__oslogstring: 0x3fb
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0x124
   __TEXT.__objc_methname: 0x18fd
   __TEXT.__objc_methtype: 0x4f7

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x760
+  __DATA_CONST.__objc_selrefs: 0x7e8
   __DATA_CONST.__objc_superrefs: 0x40
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x1180
+  __AUTH_CONST.__objc_const: 0xea8
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08A44127-D26E-38B2-A025-56FE5B102127
-  Functions: 209
-  Symbols:   686
+  UUID: C2B99FCA-5C2C-376D-AEC7-6F85A3F6AD3E
+  Functions: 228
+  Symbols:   710
   CStrings:  605
 
Symbols:
+ +[BKSProcess currentProcess].cold.1
+ +[BKSWorkspace sharedInstance].cold.1
+ -[BKSApplicationStateMonitor applicationInfoForApplication:completion:].cold.1
+ -[BKSApplicationStateMonitor applicationInfoForPID:completion:].cold.1
+ -[BKSApplicationStateMonitor initWithEndpoint:bundleIDs:states:elevatedPriority:].cold.1
+ -[BKSApplicationStateMonitor updateInterestedBundleIDs:states:].cold.1
+ -[BKSProcess _bootstrapWithError:].cold.1
+ -[BKSProcess bootstrapWithProcessHandle:error:].cold.1
+ -[BKSProcess bootstrapWithProcessHandle:error:].cold.2
+ -[BKSProcess bootstrapWithProcessHandle:error:].cold.3
+ -[BKSProcess initWithBundleIdentifier:].cold.1
+ -[BKSProcess initWithBundleIdentifier:].cold.2
+ -[BKSProcess initWithProcessIdentity:].cold.1
+ -[BKSProcess initWithProcessIdentity:].cold.2
+ BKSProcessAssertionSetExpirationHandler.cold.2
+ BKSProcessAssertionSetExpirationHandler.cold.3
+ BKSWatchdogAssertionCreateForPID.cold.1
+ RBSProcessLegacyStateDescriptor.cold.1
+ _BKSWatchdogAssertionGetTypeID.cold.1
+ __observerManager.cold.1

```
