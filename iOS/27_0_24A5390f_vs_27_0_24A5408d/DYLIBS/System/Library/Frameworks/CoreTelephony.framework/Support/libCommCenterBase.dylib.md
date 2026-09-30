## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13482.1.0.0.0
-  __TEXT.__text: 0xd228c
+13487.3.0.0.0
+  __TEXT.__text: 0xd2ff4
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0xd2e0
-  __TEXT.__cstring: 0x14a9d
-  __TEXT.__gcc_except_tab: 0x13b38
-  __TEXT.__oslogstring: 0x25ef
-  __TEXT.__unwind_info: 0x4e48
+  __TEXT.__const: 0xd370
+  __TEXT.__cstring: 0x14ac8
+  __TEXT.__gcc_except_tab: 0x13be4
+  __TEXT.__oslogstring: 0x2849
+  __TEXT.__unwind_info: 0x4e60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76d0
+  __DATA_CONST.__const: 0x76e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x218
-  __AUTH_CONST.__const: 0x14470
-  __AUTH_CONST.__cfstring: 0x2cc0
+  __AUTH_CONST.__const: 0x14480
+  __AUTH_CONST.__cfstring: 0x2ce0
   __AUTH_CONST.__objc_const: 0x200
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_got: 0xc38
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x68
+  __DATA.__data: 0x70
   __DATA.__bss: 0x5
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x18

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5760
-  Symbols:   9489
-  CStrings:  4486
+  Functions: 5765
+  Symbols:   9507
+  CStrings:  4497
 
Symbols:
+ __ZN16CSIPacketAddress36getAddressDefaultGatewayForInterfaceEPKciRS_
+ __ZNK16CSIPacketAddress23isPublicRoutableAddressEv
+ __ZNK16CSIPacketAddress28isDefaultGatewayForInterfaceERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9foe220106EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
+ __ZZN12_GLOBAL__N_120isPublicRoutableIPv4EjE9kReserved
+ __ZZN16CSIPacketAddress36getAddressDefaultGatewayForInterfaceEPKciRS_E6rtmSeq
+ _getpid
+ _if_nametoindex
+ _objc_enumerationMutation
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_release_x27
+ _read
+ _send
+ _strerror
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
```
