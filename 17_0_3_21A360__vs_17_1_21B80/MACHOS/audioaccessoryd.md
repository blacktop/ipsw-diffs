## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-443.1.5.0.0
-  __TEXT.__text: 0x159594
+456.0.0.0.0
+  __TEXT.__text: 0x1598b8
   __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_stubs: 0xb880
-  __TEXT.__objc_methlist: 0x4974
+  __TEXT.__objc_stubs: 0xb8c0
+  __TEXT.__objc_methlist: 0x49d4
   __TEXT.__const: 0x2e94
-  __TEXT.__gcc_except_tab: 0x23e0
-  __TEXT.__cstring: 0x22323
-  __TEXT.__objc_methname: 0x10beb
-  __TEXT.__objc_classname: 0x580
-  __TEXT.__objc_methtype: 0x205a
-  __TEXT.__oslogstring: 0x82aa
+  __TEXT.__gcc_except_tab: 0x23dc
+  __TEXT.__cstring: 0x224d3
+  __TEXT.__objc_methname: 0x10d97
+  __TEXT.__objc_classname: 0x581
+  __TEXT.__objc_methtype: 0x2073
+  __TEXT.__oslogstring: 0x82ae
   __TEXT.__constg_swiftt: 0x12cc
   __TEXT.__swift5_typeref: 0x16ce
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift5_capture: 0x1b08
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3808
+  __TEXT.__unwind_info: 0x3820
   __TEXT.__eh_frame: 0x18a8
   __DATA_CONST.__auth_got: 0x12b8
   __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0x98
   __DATA_CONST.__const: 0x9570
-  __DATA_CONST.__cfstring: 0x61e0
+  __DATA_CONST.__cfstring: 0x61c0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_dictobj: 0x488
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xc890
-  __DATA.__objc_selrefs: 0x39d0
+  __DATA.__objc_const: 0xc980
+  __DATA.__objc_selrefs: 0x3a10
   __DATA.__objc_protorefs: 0x78
-  __DATA.__objc_classrefs: 0x510
+  __DATA.__objc_classrefs: 0x518
   __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0xaac
+  __DATA.__objc_ivar: 0xac4
   __DATA.__objc_data: 0x1648
   __DATA.__data: 0x2c20
   __DATA.__bss: 0x56f0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5108
-  Symbols:   1032
-  CStrings:  7287
+  Functions: 5116
+  Symbols:   1033
+  CStrings:  7311
 
Symbols:
+ _OBJC_CLASS_$_TUCall
CStrings:
+ "\x01!!\x11R\x12%#2\x11\x111!\x11\x11\x13\x126\x13\x13\x11\x12\xb1a\x111\x12$1!!H\x11\x12\x13\"\x11\x13\x18"
+ "###Hijackblocking: Hijack request from remote, device %@ hijack block with %ll{dur} remaining with ticks %lld"
+ "-[AAServicesDaemon _createBannerSessionMuteActionForIOS:auditToken:appName:appBundleID:]"
+ "-[BTSmartRoutingDaemon _cancelTriangleRecoveryTimer]"
+ "-[BTSmartRoutingDaemon isInAnyTipi]_block_invoke"
+ "Checking Tipi state of Wx %@ uuid %@ sourceCount %u otherTipi %@ inTipi %s"
+ "Hijackblocking: Hijack Request, device %@ with %ll{dur} remaining, last ticks are %llu"
+ "Hijackblocking: Relay message from remote updates hijack blocking ticks, device %@ hijack block with %ll{dur} remaining, last ticks %llu"
+ "MUC - generated keys with V2 RSA: %@"
+ "Mute Control: Cannot show reject banner, invalid audio owner device: %@"
+ "REJECTED_WITH_DEVICE_FORMAT"
+ "TB,N,V_autoConnectForXR"
+ "TB,N,V_nearbyBannerActionConnect"
+ "TB,N,V_nearbyBannerShown"
+ "TUNotification: Call state changed incoming %s outgoing %s status %s endpoint %s uuid %@"
+ "TUNotification: Received call changed %@"
+ "TriangleRecovery: Magnet %s inAnyTipi %s TipiInProgress %s"
+ "TriangleRecovery: Skip, timer exists"
+ "TriangleRecovery: SrDeviceNearby %s magnet %s inAnyTipi %s timeout %d"
+ "^{__CFUserNotification=}"
+ "_autoConnectForXR"
+ "_cancelTriangleRecoveryTimer"
+ "_nearbyBannerActionConnect"
+ "_nearbyBannerShown"
+ "_prefxrOSConnectedAudioNotifications"
+ "_uiNoteSessionSmartRoutingXROS"
+ "_uiNoteSessionSmartRoutingXROSType"
+ "autoConnectForXR"
+ "isInAnyTipi"
+ "nearbyBannerActionConnect"
+ "nearbyBannerShown"
+ "setAutoConnectForXR:"
+ "setNearbyBannerActionConnect:"
+ "setNearbyBannerShown:"
- "\x01!!\x11R\x12%#2\x11\x111!\x11\x11\x13\x126\x13\x13\x11\x12\xb1a\x111\x12$1!!H\x11\x12\x13\"\x13\x18"
- "###Hijackblocking: Hijack request from remote, device %@ hijack block with %llu{dur} remaining with ticks %lld"
- "Hijackblocking: Hijack Request, device %@ with %llu{dur} remaining, last ticks are %llu"
- "Hijackblocking: Relay message from remote updates hijack blocking ticks, device %@ hijack block with %llu{dur} remaining, last ticks %llu"
- "MUC - generated keys for RSA: %@"
- "REJECTED"
- "TUNotification: Call state changed incmoing %s outgoing %s status %s endpoint %s uuid %@"
- "TriangleRecovery: Magnet %s inTipi %s TipiInProgress %s"
- "TriangleRecovery: SrDeviceNearby %s magnet %s inTipi %s timeout %d"
- "reject"

```
