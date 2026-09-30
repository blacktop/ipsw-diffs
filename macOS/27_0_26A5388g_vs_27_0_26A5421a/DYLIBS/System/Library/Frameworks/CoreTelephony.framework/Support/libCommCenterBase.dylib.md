## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13482.0.0.0.0
-  __TEXT.__text: 0xd1750
+13487.1.0.0.0
+  __TEXT.__text: 0xd1eac
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0xd2e0
-  __TEXT.__cstring: 0x1340b
-  __TEXT.__gcc_except_tab: 0x13b30
-  __TEXT.__oslogstring: 0x25ef
-  __TEXT.__unwind_info: 0x4de8
+  __TEXT.__const: 0xd360
+  __TEXT.__cstring: 0x13261
+  __TEXT.__gcc_except_tab: 0x13bc0
+  __TEXT.__oslogstring: 0x26f1
+  __TEXT.__unwind_info: 0x4e00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x75e0
+  __DATA_CONST.__const: 0x75f0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x208
-  __AUTH_CONST.__const: 0x14480
-  __AUTH_CONST.__cfstring: 0x2ca0
+  __AUTH_CONST.__const: 0x14458
+  __AUTH_CONST.__cfstring: 0x2cc0
   __AUTH_CONST.__objc_const: 0x200
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xb88
+  __AUTH_CONST.__auth_got: 0xbb0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x68
+  __DATA.__data: 0x70
   __DATA.__bss: 0x5
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x18

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5757
-  Symbols:   9471
-  CStrings:  4445
+  Functions: 5762
+  Symbols:   9487
+  CStrings:  4443
 
Symbols:
+ __ZN16CSIPacketAddress36getAddressDefaultGatewayForInterfaceEPKciRS_
+ __ZNK16CSIPacketAddress23isPublicRoutableAddressEv
+ __ZNK16CSIPacketAddress28isDefaultGatewayForInterfaceERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9nqe220106EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
+ __ZZN12_GLOBAL__N_120isPublicRoutableIPv4EjE9kReserved
+ __ZZN16CSIPacketAddress36getAddressDefaultGatewayForInterfaceEPKciRS_E6rtmSeq
+ ___TUAssertTrigger
+ _getpid
+ _if_nametoindex
+ _objc_enumerationMutation
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _read
+ _send
+ _strerror
- __ZNK3xpc6object9to_stringEv
- __os_log_debug_impl
CStrings:
+ "[%s]getAddressDefaultGatewayForInterface: has no default route: %s (%d)"
+ "[%s]getAddressDefaultGatewayForInterface: if_nametoindex failed %s"
+ "[%s]getAddressDefaultGatewayForInterface: ioctl FIONBIO failed %s"
+ "[%s]getAddressDefaultGatewayForInterface: read failed %s (%d)"
+ "[%s]getAddressDefaultGatewayForInterface: route socket setup failed %s"
+ "[%s]getAddressDefaultGatewayForInterface: send failed %s (%d)"
+ "[%s]getAddressDefaultGatewayForInterface: unknown GW: %s (%d)"
+ "[%s]getAddressDefaultGatewayForInterface: unknown IP family1: %s (%d)"
+ "[%s]getAddressDefaultGatewayForInterface: unknown IP family2: %s (%d)"
+ "kPhone"
+ "lastSuccessfulActiveIccidTimestamps"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"
- "DisplayStatus [isOn=%{bool}d, isLocked=%{bool}d, isCoversheetActive=%{bool}d, isPasscodeSet=%{bool}d, isEffectivelyLocked=%{bool}d]"
- "Getting main bundle"
- "Input(%s) = %f"
- "Parsed %zu lines successfully"
- "Personality Info: %s - %s"
- "Sending OTASP success dialogue to UI"
- "ThumperID: %s, info: %p"
- "[conn %p] Connection closed."
- "[conn %p] Got REST message: %s"
- "not active"
```
