## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0x1f840
+  __TEXT.__text: 0x23524
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1d8
   __TEXT.__gcc_except_tab: 0x24d8
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x54da
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x5661
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
+ _encryptFDRDataForBrunor
+ _getBrunorPermanentKey
+ _signDataWithBrunorCollectionKey
+ _getAttestationToBrunorCollectionKey
+ _setDummyWrappedFDRDataEncryptionKey
+ _getBrunorCollectionKey
+ _prepareFDRDataEncryptionKey
+ _signDataWithBrunorPermanentKey
CStrings:
+ "PSD3MACLength == (16)"
+ "getAttestationToBrunorCollectionKey -> %!d(MISSING)\n"
+ "attestationLength"
+ "prepareFDRDataEncryptionKey\n"
+ "outPSD3Length"
+ "reply"
+ "setDummyWrappedFDRDataEncryptionKey\n"
+ "signature"
+ "getAttestationToBrunorCollectionKey\n"
+ "getBrunorPermanentKey\n"
+ "*signature"
+ "signatureLength"
+ "encryptFDRDataForBrunor %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING) %!p(MISSING) %!z(MISSING)u\n"
+ "replySize <= sizeof(reply)"
+ "PSD3"
+ "signDataWithBrunorPermanentKey -> %!d(MISSING)\n"
+ "permanentKeyLength"
+ "setDummyWrappedFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "*attestation"
+ "collectionKeyLength"
+ "getBrunorCollectionKey -> %!d(MISSING)\n"
+ "replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)"
+ "getBrunorCollectionKey\n"
+ "dataLength"
+ "attestation"
+ "PSD2Length"
+ "replySize <= (16 * 1024)"
+ "collectionKey"
+ "signDataWithBrunorPermanentKey\n"
+ "getBrunorPermanentKey -> %!d(MISSING)\n"
+ "PSD2"
+ "permanentKey"
+ "prepareFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "signDataWithBrunorCollectionKey\n"
+ "signDataWithBrunorCollectionKey -> %!d(MISSING)\n"
+ "replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)"
+ "encryptFDRDataForBrunor -> %!d(MISSING)\n"

```
