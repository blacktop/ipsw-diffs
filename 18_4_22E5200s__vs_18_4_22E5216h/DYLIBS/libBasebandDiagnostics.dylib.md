## libBasebandDiagnostics.dylib

> `/usr/lib/libBasebandDiagnostics.dylib`

```diff

-1245.0.0.0.0
-  __TEXT.__text: 0xbce4
-  __TEXT.__auth_stubs: 0x850
+1248.0.0.0.0
+  __TEXT.__text: 0xd2fc
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x338
-  __TEXT.__gcc_except_tab: 0x12d8
-  __TEXT.__cstring: 0xbc8
-  __TEXT.__oslogstring: 0x5ff
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__gcc_except_tab: 0x1540
+  __TEXT.__cstring: 0xd49
+  __TEXT.__oslogstring: 0x95f
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x98
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__auth_got: 0x480
   __AUTH_CONST.__const: 0x230
-  __AUTH_CONST.__cfstring: 0xa80
+  __AUTH_CONST.__cfstring: 0xcc0
   __DATA.__data: 0x50
   __DATA.__bss: 0x10
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 141
-  Symbols:   438
-  CStrings:  230
+  Functions: 149
+  Symbols:   464
+  CStrings:  274
 
Symbols:
+ _AMAuthInstallCreate
+ _AMAuthInstallRequestSendSync
+ _CFDataCreateCopy
+ _CFDictionaryContainsKey
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _CFNumberGetTypeID
+ __ZN21BasebandRFDiagnostics22getRFSelfTestTicketINTEbjPPK8__CFData
+ __ZN21BasebandRFDiagnostics33getBasebandPersonalizationInfoINTEv
+ __ZN3abm19kKeyBasebandBoardIdE
+ __ZN3abm19kKeyBasebandUidModeE
+ __ZN3abm24kKeyBasebandSecurityModeE
+ __ZN3abm24kKeyCommandGetPersParamsE
+ __ZN3abm26kKeyBasebandProductionModeE
+ __ZN3abm26kKeyBasebandSecurityDomainE
+ __ZN3abm33kCommandPrepareBasebandRFSelfTestE
+ __ZN3xpc6bridgeERKNS_6objectE
+ __ZN6config2hw6iPhoneEv
+ __ZNK3xpc6object9to_stringEv
+ _kAMAuthInstallTagApChipId
+ _kAMAuthInstallTagApEcid
CStrings:
+ "#I Prepare Baseband for RF Self Test: %s"
+ "#I Returned the RF self test ticket: Success"
+ "#I Send the signing request"
+ "#I Signed the RF self test ticket: Success"
+ "@Cellular1,Ticket"
+ "AMAI alloc failed"
+ "AP ChipID is zero"
+ "AP ECID is zero"
+ "AP chipid cfnum conversion failure"
+ "AP ecid cfnum conversion failure"
+ "Baseband ECID data conversion failed"
+ "Cellular1,BbFieldDiagsEnable"
+ "Cellular1,BoardID"
+ "Cellular1,ChipID"
+ "Cellular1,ECID"
+ "Cellular1,Nonce"
+ "Cellular1,ProductionMode"
+ "Cellular1,SecurityDomain"
+ "Cellular1,SecurityMode"
+ "Cellular1,Ticket"
+ "Cellular1,UID_MODE"
+ "Failed to create request dictionary"
+ "Failed to get personalization parameters"
+ "Get pers parameters cmd failed: %s"
+ "Missing parameters in GetPersInfo: %s"
+ "Null data for Nonce"
+ "Null data for Prod Mode"
+ "Null data for Sec Mode"
+ "Null data for Uid Mode"
+ "Null fPersParams"
+ "Output ticket cp failed"
+ "RF self test ticket request failed with missing ticket in the response"
+ "RF self test ticket request failed with non-zero return value"
+ "RF self test ticket request failed with null return dictionary"
+ "Wrong type for Prod Mode"
+ "Wrong type for Sec Mode"
+ "Wrong type for Uid Mode"
+ "kKeyBasebandBoardId"
+ "kKeyBasebandChipID"
+ "kKeyBasebandProductionMode"
+ "kKeyBasebandSecurityDomain"
+ "kKeyBasebandSecurityMode"
+ "kKeyBasebandSerialNumber"
+ "kKeyBasebandUidMode"

```
