## demod

> `/usr/libexec/demod`

```diff

-1254.60.17.0.0
-  __TEXT.__text: 0xc98dc
-  __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_stubs: 0x16be0
-  __TEXT.__objc_methlist: 0xa44c
+1254.80.3.0.0
+  __TEXT.__text: 0xc9e04
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_stubs: 0x16ca0
+  __TEXT.__objc_methlist: 0xa4a4
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xcf4f
-  __TEXT.__objc_methname: 0x1acba
-  __TEXT.__oslogstring: 0x1599d
+  __TEXT.__cstring: 0xcfa6
+  __TEXT.__objc_methname: 0x1adde
+  __TEXT.__oslogstring: 0x15a38
   __TEXT.__objc_classname: 0x14e0
-  __TEXT.__objc_methtype: 0x353c
+  __TEXT.__objc_methtype: 0x3579
   __TEXT.__gcc_except_tab: 0x35d8
-  __TEXT.__unwind_info: 0x2950
-  __DATA_CONST.__auth_got: 0xb30
+  __TEXT.__unwind_info: 0x2960
+  __DATA_CONST.__auth_got: 0xb38
   __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2620
-  __DATA_CONST.__cfstring: 0xc0c0
+  __DATA_CONST.__const: 0x2608
+  __DATA_CONST.__cfstring: 0xc160
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x3a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x179c8
-  __DATA.__objc_selrefs: 0x64a8
+  __DATA.__objc_const: 0x17a28
+  __DATA.__objc_selrefs: 0x64f8
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0xaa0
+  __DATA.__objc_classrefs: 0xaa8
   __DATA.__objc_superrefs: 0x3a8
-  __DATA.__objc_ivar: 0x9ac
+  __DATA.__objc_ivar: 0x9b0
   __DATA.__objc_data: 0x3ca0
   __DATA.__data: 0x2328
   __DATA.__bss: 0x4e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4964
-  Symbols:   738
-  CStrings:  8988
+  Functions: 4973
+  Symbols:   740
+  CStrings:  9012
 
Symbols:
+ _IOPMAssertionRelease
+ _OBJC_CLASS_$_FBSShutdownOptions
CStrings:
+ "Device shutting down..."
+ "Failed to release power assertion."
+ "HoldPowerAssertion"
+ "LiftPowerAssertion"
+ "Lifting power assertion to enable device sleep."
+ "RebootAfterRevert"
+ "Shutdown"
+ "TB,R,GpowerAssertionActive"
+ "TI,N,V_powerAssertion"
+ "Taking power assertion to prevent device sleep."
+ "_powerAssertion"
+ "demod shutdown device"
+ "holdPowerAssertion"
+ "initWithReason:"
+ "liftPowerAssertion"
+ "powerAssertion"
+ "powerAssertionActive"
+ "revertSnapshotAndShutdown"
+ "setPowerAssertion:"
+ "setRebootType:"
+ "shutdown"
+ "shutdownWithOptions:"
+ "triggerSnapshotRevertOnPeerOfID:rebootDevice:withCompletion:"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@16B24@?28"
- "preventSleep"

```
