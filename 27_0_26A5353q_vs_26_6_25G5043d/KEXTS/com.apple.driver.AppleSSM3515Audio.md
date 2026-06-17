## com.apple.driver.AppleSSM3515Audio

> `com.apple.driver.AppleSSM3515Audio`

```diff

-1000.40.0.0.0
+940.17.0.0.0
   __TEXT.__const: 0x18 sha256:85a6f21e9614cc02a040510501f05efe3f8512e86486c14feefcd3b3763dcb4a
-  __TEXT.__cstring: 0x5d2 sha256:b6eb27f4a194e5c06df80b2b8c82c760e7cf8b38953643ea4b4d2b504ea9d365
+  __TEXT.__cstring: 0x477 sha256:95200e51d61c78d8e547477188c9687c31eb4ee5b2d44c52dc6fa2c8d9945e41
   __TEXT.__os_log: 0x2d0 sha256:01706b400222c371e2414b4a854c5495dc8b13a3466ca996c41432a6e9649053
-  __TEXT_EXEC.__text: 0x2734 sha256:912bbdaf3e48385966aae492be79cfaea095dd0400e3050db22851885d197423
+  __TEXT_EXEC.__text: 0x26d0 sha256:be4a8e1de0a61a4ed10077c95ff9a85bcae7f6ec204891565cd2637f5d7c37f5
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:f85e4102d0ff6d40285de90278c50ce7059fa85529a91359d8946355f4372485
+  __DATA.__data: 0xc8 sha256:7c93b2d151d956d13614888262820303fbd349fcdc0bde570303a4d14a1e2d23
   __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__mod_init_func: 0x8 sha256:983d71676eb581f9296832b854a51853b24c18ef151af3c4b8570a74461410c0
-  __DATA_CONST.__mod_term_func: 0x8 sha256:6be7f44fc86ee8f2b715daff8a41a07dfabe5f6060b76fdc396bbbf232aff26f
-  __DATA_CONST.__const: 0xfe8 sha256:56c9c1350aad5a35f987aedb46e721dfade6bd65bf5b418f5fe4f4c89801ecbb
-  __DATA_CONST.__kalloc_type: 0x40 sha256:dd32514618f11d2b09974decafe004d5cd4491b32b77e0a47b9cde3dd02a4026
-  __DATA_CONST.__auth_got: 0xb8 sha256:8909d2a29a4d68ec7acac421d55bd0e491854ffbf14daeb9c44f8a6ad3c16e95
-  __DATA_CONST.__got: 0x30 sha256:2004257fc396d4f476824d00890084de60bfc01fae2b9814170ea6ed80d629c3
-  UUID: BF154DCD-0F69-3150-B9A4-07ECC577D209
-  Functions: 77
-  Symbols:   584
-  CStrings:  60
+  __DATA_CONST.__auth_got: 0xa8 sha256:3bb8a02329aab0ac29d6c303f5965cf4caf266d3eba990eafdd97a1d67d693ad
+  __DATA_CONST.__got: 0x30 sha256:291a49a03f890a8b86c3e4ddb40b9a96281468fdd6f1564da179d4f99e5aa7f6
+  __DATA_CONST.__auth_ptr: 0x8 sha256:2cad330ce9beaf9d9ca1621fac2ef6f424d3dcdc8f23e4af30fb226743749e75
+  __DATA_CONST.__mod_init_func: 0x8 sha256:6ca3bc6cb0953a52b3799090170d3a201b075d102bbb0062aebacdbe45768a32
+  __DATA_CONST.__mod_term_func: 0x8 sha256:dee548f01057fe441f1c039c80dfa137730fa4c435f52683b9f25668ef70196e
+  __DATA_CONST.__const: 0xfe0 sha256:8abaaa8e3e6cefeabb2ca6dd842eef81ba4e38ff06f4ab3b0ed2601d0781c1c0
+  __DATA_CONST.__kalloc_type: 0x40 sha256:ea427a17375fe3d0a1ff7f167da892b45ae7547ddbb960b19c956c84ecad64cc
+  UUID: 13E4CE62-90E1-35C1-8787-15D22BFF5C91
+  Functions: 75
+  Symbols:   577
+  CStrings:  55
 
Symbols:
+ __ZN17AppleSSM3515Audio15_getSerialBytesEhhhRhPch
+ ___chkstk_darwin
+ ___chkstk_darwin_probe
+ _bzero
- _IOFreeData
- _IOMallocData
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.2
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.3
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.4
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.5
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.6
- _ZN17AppleSSM3515Audio32_getSerialNumberForIORegPropertyEv.cold.7
- __ZN18AppleEmbeddedAudio20getIISBitsPerChannelEj
- __ZN9os_detail21panic_trapping_policy4trapEPKc
- _panic
CStrings:
- "\"%s\" @%s:%d"
- "OSBoundedPtr.h"
- "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
- "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
- "bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally"

```
