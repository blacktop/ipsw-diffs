## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-12317.2.0.0.0
-  __TEXT.__text: 0x54134
-  __TEXT.__auth_stubs: 0x1050
+12320.0.0.0.0
+  __TEXT.__text: 0x542d4
+  __TEXT.__auth_stubs: 0x1080
   __TEXT.__const: 0x2487
-  __TEXT.__gcc_except_tab: 0x41c0
-  __TEXT.__cstring: 0x2525
-  __TEXT.__oslogstring: 0x78c2
-  __TEXT.__unwind_info: 0x1988
+  __TEXT.__gcc_except_tab: 0x41b8
+  __TEXT.__cstring: 0x24ea
+  __TEXT.__oslogstring: 0x7884
+  __TEXT.__unwind_info: 0x1980
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x2b40
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__const: 0x2b48
+  __AUTH_CONST.__cfstring: 0x7c0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1155
-  Symbols:   1583
-  CStrings:  1155
+  Symbols:   1586
+  CStrings:  1152
 
Symbols:
+ _TelephonyUtilIsOversteerEnabled
+ __ZN16CSIPacketAddressaSERKS_
+ __ZN2sd18IMSSubscriberModel15updatePcscfListERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEERKS8_
+ __ZN2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_
+ __ZNK2sd18IMSSubscriberModel10isUsingTlsEv
+ __ZNK2sd19IMSSubscriberConfig15getRTTSupportedEb
+ __ZNK2sd19IMSSubscriberConfig24getEmergencyRTTSupportedEb
+ __ZNK2sd23IMSSubscriberController10isUsingTlsEv
+ __ZThn48_N2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_
+ __ZThn48_NK2sd23IMSSubscriberController10isUsingTlsEv
+ _memchr
- __ZN2sd18IMSSubscriberModel15updatePcscfListERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEERKS8_jj
- __ZN2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_jj
- __ZNK2sd18IMSSubscriberModel12getPcscfPortEv
- __ZNK2sd19IMSSubscriberConfig15getRTTSupportedEv
- __ZNK2sd19IMSSubscriberConfig24getEmergencyRTTSupportedEv
- __ZNK2sd19IMSSubscriberConfig30getRcsPinnedCertificateDigestsEv
- __ZThn48_N2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_jj
CStrings:
+ "#I 5wi.mdl:: \t fUEInfo: [[IsimInfo: fIsPresent = %s, fIsAllFilesRead = %s, fImpi = %s, fImpuList = %s, fDomain = %s, fPcscfList = %s, fPcscfDomain = %s], [fDeviceInfo: fImsi = %s, fMdn = %s, fIsSimPersonality = %s, fDeviceId = %s, fDeviceSVN = %s, fMcc = %s, fMnc = %s, fUSimPresent = %s]]"
- "#I 5wi.mdl:: \t fUEInfo: [[IsimInfo: fIsPresent = %s, fIsAllFilesRead = %s, fImpi = %s, fImpuList = %s, fDomain = %s, fPcscfList = %s, fPcscfDomain = %s, fPcscfPort = %u], [fDeviceInfo: fImsi = %s, fMdn = %s, fIsSimPersonality = %s, fDeviceId = %s, fDeviceSVN = %s, fMcc = %s, fMnc = %s, fUSimPresent = %s]]"
- "#I RCS Pinned certificate digests %{public}@"
- "PinnedCertificateDigests"
- "RcsCertificatePublicKeyDigestList"

```
