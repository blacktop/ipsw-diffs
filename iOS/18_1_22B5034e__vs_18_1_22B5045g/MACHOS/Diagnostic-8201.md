## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0x1f800
+  __TEXT.__text: 0x234e4
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1d8
   __TEXT.__gcc_except_tab: 0x24c4
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x54b7
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x563e
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methname: 0xb35
   __TEXT.__objc_methtype: 0x6b3
-  __TEXT.__oslogstring: 0x6ae
+  __TEXT.__oslogstring: 0x8d2
   __TEXT.__unwind_info: 0x5e8
   __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0x350

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   395
-  CStrings:  889
+  Functions: 253
+  Symbols:   403
+  CStrings:  926
 
Symbols:
+ _setDummyWrappedFDRDataEncryptionKey
+ _signDataWithBrunorCollectionKey
+ _getBrunorPermanentKey
+ _getAttestationToBrunorCollectionKey
+ _signDataWithBrunorPermanentKey
+ _prepareFDRDataEncryptionKey
+ _getBrunorCollectionKey
+ _encryptFDRDataForBrunor
CStrings:
+ "signature"
+ "encryptFDRDataForBrunor -> %!d(MISSING)\n"
+ "replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)"
+ "PSD3"
+ "*attestation"
+ "permanentKey"
+ "prepareFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "getBrunorCollectionKey\n"
+ "attestationLength"
+ "signDataWithBrunorCollectionKey -> %!d(MISSING)\n"
+ "replySize <= (16 * 1024)"
+ "reply"
+ "*signature"
+ "setDummyWrappedFDRDataEncryptionKey\n"
+ "replySize <= sizeof(reply)"
+ "setDummyWrappedFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "collectionKey"
+ "prepareFDRDataEncryptionKey\n"
+ "permanentKeyLength"
+ "getBrunorPermanentKey -> %!d(MISSING)\n"
+ "PSD2Length"
+ "getBrunorPermanentKey\n"
+ "PSD2"
+ "signDataWithBrunorPermanentKey\n"
+ "signatureLength"
+ "outPSD3Length"
+ "replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)"
+ "getAttestationToBrunorCollectionKey -> %!d(MISSING)\n"
+ "signDataWithBrunorCollectionKey\n"
+ "encryptFDRDataForBrunor %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING) %!p(MISSING) %!z(MISSING)u\n"
+ "getAttestationToBrunorCollectionKey\n"
+ "getBrunorCollectionKey -> %!d(MISSING)\n"
+ "collectionKeyLength"
+ "signDataWithBrunorPermanentKey -> %!d(MISSING)\n"
+ "attestation"
+ "PSD3MACLength == (16)"
+ "dataLength"

```
