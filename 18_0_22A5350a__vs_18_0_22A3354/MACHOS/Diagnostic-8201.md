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
+ _getBrunorCollectionKey
+ _signDataWithBrunorCollectionKey
+ _encryptFDRDataForBrunor
+ _signDataWithBrunorPermanentKey
+ _setDummyWrappedFDRDataEncryptionKey
+ _prepareFDRDataEncryptionKey
+ _getAttestationToBrunorCollectionKey
+ _getBrunorPermanentKey
CStrings:
+ "prepareFDRDataEncryptionKey\n"
+ "collectionKey"
+ "attestationLength"
+ "getBrunorCollectionKey\n"
+ "setDummyWrappedFDRDataEncryptionKey\n"
+ "signature"
+ "*attestation"
+ "setDummyWrappedFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "*signature"
+ "PSD2Length"
+ "replySize <= (16 * 1024)"
+ "getBrunorCollectionKey -> %!d(MISSING)\n"
+ "getAttestationToBrunorCollectionKey\n"
+ "replySize <= sizeof(reply)"
+ "PSD3MACLength == (16)"
+ "reply"
+ "getBrunorPermanentKey -> %!d(MISSING)\n"
+ "permanentKey"
+ "outPSD3Length"
+ "prepareFDRDataEncryptionKey -> %!d(MISSING)\n"
+ "getBrunorPermanentKey\n"
+ "encryptFDRDataForBrunor -> %!d(MISSING)\n"
+ "signatureLength"
+ "signDataWithBrunorCollectionKey\n"
+ "PSD3"
+ "getAttestationToBrunorCollectionKey -> %!d(MISSING)\n"
+ "signDataWithBrunorPermanentKey\n"
+ "attestation"
+ "PSD2"
+ "permanentKeyLength"
+ "dataLength"
+ "signDataWithBrunorCollectionKey -> %!d(MISSING)\n"
+ "encryptFDRDataForBrunor %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING) %!p(MISSING) %!z(MISSING)u\n"
+ "replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)"
+ "signDataWithBrunorPermanentKey -> %!d(MISSING)\n"
+ "collectionKeyLength"
+ "replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)"

```
