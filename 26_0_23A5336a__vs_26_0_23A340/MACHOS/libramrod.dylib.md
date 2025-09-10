## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

 3476.2.1.0.0
-  __TEXT.__text: 0xd9310
+  __TEXT.__text: 0xdb2d0
   __TEXT.__auth_stubs: 0x2830
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__cstring: 0x286e1
+  __TEXT.__cstring: 0x288ad
   __TEXT.__const: 0x94960
   __TEXT.__gcc_except_tab: 0xbb4
-  __TEXT.__oslogstring: 0x9e5
-  __TEXT.__unwind_info: 0x1c90
+  __TEXT.__oslogstring: 0xab1
+  __TEXT.__unwind_info: 0x1cc8
   __TEXT.__eh_frame: 0x3c0
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methname: 0x2901

   __DATA_CONST.__objc_selrefs: 0xc90
   __AUTH_CONST.__auth_got: 0x1430
   __AUTH_CONST.__const: 0x1fd0
-  __AUTH_CONST.__cfstring: 0xb500
+  __AUTH_CONST.__cfstring: 0xb540
   __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x2b8
+  __AUTH.__data: 0x2e8
   __DATA.__objc_classrefs: 0x128
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x134

   - /usr/lib/libpartition2_dynamic.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 02BCE1BF-7FA9-3AF7-B5FA-8BCEEBA9CB79
-  Functions: 2593
-  Symbols:   1794
-  CStrings:  7336
+  UUID: E340FA70-16AF-3020-80A7-CDAB2D2929CE
+  Functions: 2620
+  Symbols:   1800
+  CStrings:  7364
 
Symbols:
+ _generateAndVerifyAriesHostAuthorization
+ _getAttestationToPDAK
+ _getDummy0PSDData
+ _getPDAK
+ _ramrod_device_has_centauri
+ _ramrod_should_update_centauri
CStrings:
+ "(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))"
+ "/usr/lib/updaters/libCentauriUpdater.dylib"
+ "Centauri"
+ "Skipping Centauri update since it's not present\n"
+ "Skipping checking Centauri in NeRD for bootedUpdate=true\n"
+ "att"
+ "attestation && attestationLength"
+ "centauri"
+ "clearBuffer"
+ "encryptedBuffer"
+ "generateAndVerifyAriesHostAuthorization\n"
+ "generateAndVerifyAriesHostAuthorization -> %d\n"
+ "getAttestationToPDAK\n"
+ "getAttestationToPDAK -> %d\n"
+ "getDummy0PSDData\n"
+ "getDummy0PSDData -> %d\n"
+ "getPDAK\n"
+ "getPDAK -> %d\n"
+ "no"
+ "outData"
+ "outDataLength"
+ "pdak && pdakLength"
+ "ramrod_device_has_centauri"
+ "replySize == sizeof(*outData)"
+ "replySize >= sizeof(*outData)"
+ "update_centauri"

```
