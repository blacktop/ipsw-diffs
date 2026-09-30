# 26.1 (23B82) .vs 26.1 (23B85)

## IPSWs

- `iPhone18,1_26.1_23B82_Restore.ipsw`
- `iPhone18,1_26.1_23B85_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.1 *(23B82)* | 25.1.0 | 12377.42.6~55 | Thu, 23Oct2025 11:12:58 PDT |
| 26.1 *(23B85)* | 25.1.0 | 12377.42.6~55 | Thu, 23Oct2025 11:12:58 PDT |

## MachO

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### archive.metallib

>  `/System/Library/Frameworks/ImageIO.framework/archive.metallib`

```diff

 
   __TEXT.__reflection: 0x64b0
-  __TEXT.__compute: 0x34220
+  __TEXT.__compute: 0x34230
   __TEXT.__descriptor: 0x250
   __TEXT.__metallib: 0x845e0
-  UUID: F60EFF52-5058-3F3B-BF81-193BD64AD210
+  UUID: C7A5AD36-F064-38E8-9A98-72710B711D59
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### ospredictiond

>  `/usr/libexec/ospredictiond`

```diff

-234.42.1.0.0
-  __TEXT.__text: 0x5ce58
+234.42.2.0.0
+  __TEXT.__text: 0x5cf94
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x8a00
+  __TEXT.__objc_stubs: 0x8a20
   __TEXT.__objc_methlist: 0x89c0
   __TEXT.__const: 0x2f8
   __TEXT.__cstring: 0x49f3
-  __TEXT.__objc_methname: 0x13d45
-  __TEXT.__oslogstring: 0x5536
+  __TEXT.__objc_methname: 0x13d52
+  __TEXT.__oslogstring: 0x556b
   __TEXT.__objc_classname: 0xd53
   __TEXT.__objc_methtype: 0x225b
   __TEXT.__gcc_except_tab: 0xa7c

   __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA.__objc_const: 0xf7b8
-  __DATA.__objc_selrefs: 0x3870
+  __DATA.__objc_selrefs: 0x3878
   __DATA.__objc_ivar: 0xd18
   __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x720

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A9BA067-5696-3C6D-A1B7-ABB6CD291364
-  Functions: 3052
+  UUID: 2332AD4F-B980-31E0-8CA2-24A63FB32112
+  Functions: 3053
   Symbols:   256
-  CStrings:  5152
+  CStrings:  5154
 
CStrings:
+ "Computed slot: %lu out of bounds for max range: %lu "
+ "setTimeZone:"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.1 *(23B82)* | iBoot-13822.42.2 |
| 26.1 *(23B85)* | iBoot-13822.42.2 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.1 *(23B82)* | 622.2.11.10.8 |
| 26.1 *(23B85)* | 622.2.11.10.8 |

### Dylibs

#### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### ImageIO

>  `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.1.3.2.0
-  __TEXT.__text: 0x3a5f74
+2784.1.3.3.0
+  __TEXT.__text: 0x3a5fac
   __TEXT.__auth_stubs: 0x41f0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebf8
   __TEXT.__gcc_except_tab: 0x212b4
-  __TEXT.__cstring: 0x9c7d6
+  __TEXT.__cstring: 0x9c813
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd298
+  __TEXT.__unwind_info: 0xd2a0
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 813DD8C0-4C2B-3FE8-A106-7B589A0ED4DB
-  Functions: 13174
-  Symbols:   41070
-  CStrings:  24807
+  UUID: F9804EC9-D231-3D29-91A2-F923436B5AAC
+  Functions: 13175
+  Symbols:   41072
+  CStrings:  24808
 
Symbols:
+ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.1
+ ___block_literal_global.92
- ___block_literal_global.91
Functions:
~ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t : 808 -> 820
+ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.1
CStrings:
+ "*** ERROR: LZFSE decompression failed or returned zero size\n"

```

#### ManagedConfiguration

>  `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2432.42.2.0.0
-  __TEXT.__text: 0xf8dd8
+2432.42.3.0.0
+  __TEXT.__text: 0xf8dc4
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0xb1fc
   __TEXT.__const: 0x13c4

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9E0490F-8E42-340B-BD72-487887AEB887
+  UUID: AE14250B-B54E-30C5-9FAD-29C7D67288D4
   Functions: 5644
   Symbols:   17385
   CStrings:  12225
Functions:
~ +[MCRestrictionManager filterUserSettingsForPublicUse:] : 572 -> 552

```

#### OSIntelligence

>  `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-234.42.1.0.0
-  __TEXT.__text: 0x18ee0
+234.42.2.0.0
+  __TEXT.__text: 0x18ed8
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x20e0
   __TEXT.__const: 0x1a0

   __DATA_CONST.__objc_selrefs: 0x10e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x300
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x1400
   __AUTH_CONST.__objc_const: 0x2ef0
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x5a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED2A141E-60CB-3B09-A4B6-170F0C3199B7
+  UUID: 458F17B0-BC28-3C53-B833-EF8840F45E92
   Functions: 867
   Symbols:   2921
   CStrings:  1380
Symbols:
+ ___21-[_OSIBLManager init]_block_invoke.86
+ ___21-[_OSIBLManager init]_block_invoke_2.88
+ ___22-[_OSIBLManager start]_block_invoke.109
+ ___22-[_OSIBLManager start]_block_invoke.112
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.97
- ___21-[_OSIBLManager init]_block_invoke.91
- ___21-[_OSIBLManager init]_block_invoke_2.93
- ___22-[_OSIBLManager start]_block_invoke.114
- ___22-[_OSIBLManager start]_block_invoke.117
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.102
Functions:
~ ___21-[_OSIBLManager init]_block_invoke : 220 -> 212

```

#### UIKitCore

>  `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-9126.1.12.1.111
-  __TEXT.__text: 0x1a755b4
+9126.1.12.1.112
+  __TEXT.__text: 0x1a755c0
   __TEXT.__auth_stubs: 0xd9d0
   __TEXT.__delay_helper: 0x158
   __TEXT.__init_offsets: 0x4

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 46FEF81D-075E-38E2-9002-C5F285AF522D
+  UUID: A0E1CEFB-FD01-36F9-B823-51B092E4DBC6
   Functions: 173262
   Symbols:   435165
   CStrings:  181720
Functions:
~ ___73-[UIResponder(WritingToolsSupport) _shouldShowWritingToolsInCandidateBar]_block_invoke : 200 -> 212

```


</details>

## Files

### ❌ Removed

#### filesystem (1)

- `/.fseventsd/fseventsd-uuid`

## Feature Flags

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### Sonic.plist

>  `Domain/Sonic.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>XSQ</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 </dict>
 </plist>
 

```


</details>

## EOF
