## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-880.120.2.0.0
-  __TEXT.__cstring: 0x1124e sha256:385cb51a8d8713dbc0df9499e52a3398c392d8b5df58b2595674dde077946175
-  __TEXT.__const: 0x9517 sha256:3b078db09e1ba2564781548672e5c43ddb02450977d369a9d959853a92b652b4
-  __TEXT_EXEC.__text: 0x40f0c sha256:0540cf4222003342c0646ed4121d47f40bb23ce1990dcc0002dc2bbab289e168
+926.0.0.0.0
+  __TEXT.__cstring: 0x11437 sha256:9d57c6f672f05060ad517eb999612abd2be5c716b7557fd503bbb46aa340a914
+  __TEXT.__const: 0xded0 sha256:6c0ad6f9d623a27be25a312d9476d1f3eb2f6ffdfdfb7b2cd7397f4eb1250a9c
+  __TEXT_EXEC.__text: 0x419b4 sha256:b210664ecc5a874f29b56443bc20ac8da0bf51ab0c69bf785847bff86d20c0ab
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x168 sha256:3f228d82eda40795a606751e443068b44da5b7edfb36f7d05a74fbce6f99bb3a
+  __DATA.__data: 0x168 sha256:bf5d9962cdba8c5773396f7833361002630465ebd23593a4d7b519b56bba58e6
   __DATA.__common: 0xc48 sha256:9c3a23610cbe1a6c739eb0c734761208641c970d6adfcfaf2ea599163434e704
   __DATA.__bss: 0x4e sha256:5552748b5aeb500f57b3d1f4a56e4e9789198918c663e712314ea999026eb896
-  __DATA_CONST.__auth_got: 0x578 sha256:f5b508d74f9c7783e357fd060703532e336d5b49cf9aca30e433cd4b51c591ab
-  __DATA_CONST.__got: 0x138 sha256:832bc18bda18934d0f9f85f88a7893a624a0e956f433320fa1933653c358fc27
-  __DATA_CONST.__auth_ptr: 0x38 sha256:2faf5ef2c79a715b5c1409ebba782c2eae6bc26bd060fc7c8f454c6b22346fa7
-  __DATA_CONST.__mod_init_func: 0xc0 sha256:264ae83bd53b2fc00ed6b4d65cd4f9ae8c2ca77c388c955037fa560af3998225
-  __DATA_CONST.__mod_term_func: 0xc0 sha256:492a655c0d7219a11a66a2e7e133a0232c47580dcd3b5abf9d5198179f996045
-  __DATA_CONST.__const: 0x9c68 sha256:488b41d590d6c45233e9d802ab0f901c34fe4bc4b54153b7ae9aa1691c081776
-  __DATA_CONST.__kalloc_type: 0xe00 sha256:39dec4db75ac0f8dd256994332ea130b3b4f1d9fbf4af2b8e6e2c3d40845f160
-  __DATA_CONST.__kalloc_var: 0x50 sha256:e5c31832e66db481e7c964a56786e434f15e51e0c21f07c430b16f2872a4ad31
-  UUID: AACD64FC-0B89-39D2-A3E2-781FCB960BC0
-  Functions: 2490
+  __DATA_CONST.__mod_init_func: 0xc0 sha256:77f591ece6f3924cddb0ab3405d45f6af263f0c604c05613655fdeb32dfc3aa4
+  __DATA_CONST.__mod_term_func: 0xc0 sha256:a4829873f0bee9e569723ab28c56af819fc3cdf40744bba56a3b7ab44808ee9e
+  __DATA_CONST.__const: 0x9f30 sha256:96cfa00ae573dde3fa367e8133beb21b55c0d5dc550f4460d700498273426151
+  __DATA_CONST.__kalloc_type: 0xe00 sha256:bae1304117ec3c1e47e5ea2b623dc0ecd417e6067783741854f4645f3ce21905
+  __DATA_CONST.__kalloc_var: 0x50 sha256:a00ace52df09de84a73c05904d569fcc0d504f98bda858d377e0f6d7fb69a0eb
+  __DATA_CONST.__auth_got: 0x580 sha256:e5c4af888f046dda16dbb90e1f174ea08c35fc6840d87d1561af840e12a7478b
+  __DATA_CONST.__got: 0x140 sha256:90e07aa3f235e1409f586a382b1947b05886c416e58a8ab861e234dd7f1ce72c
+  __DATA_CONST.__auth_ptr: 0x38 sha256:b2e030ebca512bd6db324d3f36acd4c538333eeee7cbf922ba68c2c2641d6ee4
+  UUID: C5E17BA6-3EF2-3278-89D5-71DF49574B61
+  Functions: 2516
   Symbols:   0
-  CStrings:  1458
+  CStrings:  1470
 
CStrings:
+ "\"SEP is being asked to sleep, but was never booted.\" @%s:%d"
+ "*out_struct.size_bytes_p >= sizeof(uint8_t) * epoch_slots_len"
+ "/arm-io/sep"
+ "AppleSEP:WARNING: %s: this command is removed\n"
+ "DispatchRemovedCommand"
+ "IOReturn AppleSEPXART::_xmsgSend(XARTMessage *, xart_buffer_config *, uint32_t)"
+ "IOReturn AppleSEPXART::_xmsgSendLocked(XARTMessage *, xart_buffer_config *, uint32_t *)"
+ "axi2af_parity_enable"
+ "bool AppleSEPManager::_hasMessageBox()"
+ "bool AppleSEPXART::_shouldHaveBootMessageTimeout()"
+ "no_monitors"
+ "out_struct.size_bytes_p != nullptr"
+ "sep_node"
+ "static IOReturn AppleSEPUserClient::DispatchGetEpochs(AppleSEPUserClient *, void *, IOExternalMethodArguments *)"
+ "timeout_ms != nullptr"
- "IOReturn AppleSEPXART::_xmsgSend(XARTMessage *, xart_buffer_config *)"
- "IOReturn AppleSEPXART::_xmsgSendLocked(XARTMessage *, xart_buffer_config *)"
- "USTUFF_LEN == piece_lens[PIECE_USTUFF]"

```
