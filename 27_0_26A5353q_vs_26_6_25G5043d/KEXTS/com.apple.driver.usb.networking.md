## com.apple.driver.usb.networking

> `com.apple.driver.usb.networking`

```diff

-391.0.0.0.0
-  __TEXT.__cstring: 0x65f sha256:bf78bceaaf8b8298298a0057930cd817bf47d6960935a75b33d5dc16a04334ef
-  __TEXT_EXEC.__text: 0x3d40 sha256:d5359ad7d839416562f4edbf99ddc3d5c82943da909bbf2eeb703d955ebab2ff
+375.100.5.0.0
+  __TEXT.__cstring: 0x270 sha256:744e830d807347ad1fe7a856f5c9dcf9fd9a4e258c20d6774defaef3e82c2b00
+  __TEXT_EXEC.__text: 0x2fe4 sha256:258f4e6dfc5e71a74ac567eed9d43c5e6ed7bc62bb97c01a2acbf8a854b2ba6d
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:4204abc3327f49dffcf51186de7628b6e13de0bb2b0af917ffd4c81102b40683
+  __DATA.__data: 0xc8 sha256:2805e8512a0a33047629e2fcfd2ab9ff0cd2b8a67a27f0c0e641f64747541877
   __DATA.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_CONST.__mod_init_func: 0x8 sha256:8aa7d996ca3674983a18f47a8251d390acd4e22e2d5d260b7cf3dfc2df22a325
-  __DATA_CONST.__mod_term_func: 0x8 sha256:7dcc5b99624d15a1972fcb5d91119ba73069938ae6680803777aa2d5f0307fcc
-  __DATA_CONST.__const: 0x8a0 sha256:5f2ebceb37b9d939c8f7e73078e8ec1cf862c38c974ac4f4f90caa04ec07125a
-  __DATA_CONST.__kalloc_type: 0xc0 sha256:1cdb0035e5ed4a14fbf305e2cb20c0e5fd07b1c2f07df36e6917726d26496137
-  __DATA_CONST.__auth_got: 0x128 sha256:43ff7f24929ee7eaf79619b415334f464a45ae25aa3cd813e40f15151252f6de
-  __DATA_CONST.__got: 0x38 sha256:1831f25b2b092185bee6d4854fb60e32681cfd8fbbdf8875a89b2d9e7d71306a
-  UUID: 17920F60-6D49-3769-8AC6-504FCC4EBA1E
-  Functions: 149
-  Symbols:   279
-  CStrings:  53
+  __DATA_CONST.__auth_got: 0x128 sha256:3906d85183eaeaaa72a028b62e4337fa639e55b90f6ff48adcbd3cff4001db66
+  __DATA_CONST.__got: 0x38 sha256:5724419af33d5a82b4a0896d467dcbc4139097eb6f6365ee8bebc88aba1f3f77
+  __DATA_CONST.__mod_init_func: 0x8 sha256:a5ed8b8589399cfd77577215974ff178d3a905909181af568785f1d78f8d8199
+  __DATA_CONST.__mod_term_func: 0x8 sha256:1bcea1e62f196be81aac6e131d0afd2f160d72cadc7f821c5a81a9e57d099bb4
+  __DATA_CONST.__const: 0x878 sha256:752bb7eb5a89dedf5c8ba6cb4c9989ef085ffb31fad232fbd8c11ac749589941
+  __DATA_CONST.__kalloc_type: 0xc0 sha256:9e1ba2cac2db3ba70a95f427ee5215a190e91f509e624e3f1c32e2c47c1e14a8
+  UUID: CF7598AA-D44A-3014-92AA-04859EABE48B
+  Functions: 118
+  Symbols:   249
+  CStrings:  26
 
Symbols:
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- __ZN18AppleUSBNCMDecoder9decodeNTBI12NTBXRxFormatEEiPKhmPj
- __ZN18AppleUSBNCMDecoder9decodeNTBI12NTBXTxFormatEEiPKhmPj
- __ZN18AppleUSBNCMEncoder9encodeNTBI12NTBXRxFormatEEiPhmPjPm
- __ZN18AppleUSBNCMEncoder9encodeNTBI12NTBXTxFormatEEiPhmPjPm
- _dumpExtendedCapabilityDescriptor
- _dumpExtendedFeatureDescriptor
CStrings:
- "\n"
- " (Medium Handling)\n"
- " (Presence Offload)\n"
- " (Receive Offload)\n"
- " (Transmit Offload)\n"
- " (Unknown)\n"
- " (Wake)\n"
- "%02x "
- "%s    WARNING: Unexpected descriptor subtype (expected 0x%02x)\n"
- "%s    WARNING: Unexpected descriptor type (expected 0x%02x)\n"
- "%s  Additional data (%u bytes): "
- "%s  WARNING: Buffer length (%u) smaller than total descriptor length (%u)\n"
- "%s  WARNING: Descriptor length too small (minimum %u)\n"
- "%s  WARNING: Feature descriptor %u extends beyond buffer (offset %u + length %u > buffer %u)\n"
- "%s  WARNING: Feature descriptor %u has invalid length %u (minimum %u)\n"
- "%s  WARNING: Not enough data for feature descriptor %u at offset %u\n"
- "%s  WARNING: Unexpected descriptor subtype (expected 0x%02x)\n"
- "%s  WARNING: Unexpected descriptor type (expected 0x%02x)\n"
- "%s  bDescriptorSubtype: 0x%02x\n"
- "%s  bDescriptorType: 0x%02x\n"
- "%s  bLength: %u\n"
- "%s  bNcmFeatureSelector: 0x%02x"
- "%s  wTotalLength: %u\n"
- "%sNCM Extended Capability Descriptor:\n"
- "%sNCM Extended Feature Descriptor %u:\n"
- "%sTotal feature descriptors found: %u\n"
- "..."

```
