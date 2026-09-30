## com.apple.driver.AppleEpochManager

> `com.apple.driver.AppleEpochManager`

```diff

-11.0.0.0.0
-  __TEXT.__cstring: 0x93a sha256:1f5a9eafee4fb317d3aba21f2788d2629043d98e340c2f0bf3d559e8e1d1e28f
+14.0.0.0.0
+  __TEXT.__cstring: 0x953 sha256:3ca0a30d60904d1586afd2448f5755fa86d79915225cf35239d85273fa794607
   __TEXT.__const: 0x38 sha256:b369aabff06509b19c744acc3bde14807aef8a39fcc92d236aaa63dfd43d34d5
-  __TEXT_EXEC.__text: 0x1aec sha256:f26141850fc1899b02b893c3cf1ef179aae893a13c44b66b1349dfa4e188ec2c
+  __TEXT_EXEC.__text: 0x1aa8 sha256:12b0b2b30bad2e27fe3c72abdf535437ae152324f5a765fd153260b992ea3475
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd0 sha256:e34ccc62289b72ec62328fe7b5c46297f02d5a19379a63446cfea6d720ff5415
+  __DATA.__data: 0xd0 sha256:1370343776f4866f2645cb61034ab3fa2649cc1c217f5a1ea3f0c280c013d472
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA_CONST.__auth_got: 0xf8 sha256:6549c18d142df9f306e4dec6d1565b0488162d7453c79b755435b5e98e12767a
-  __DATA_CONST.__got: 0x40 sha256:1124f6a93ad2ef45803396c4b66c124201a7f51ae4c557f168b9fde61fbf0575
-  __DATA_CONST.__mod_init_func: 0x10 sha256:85742a6d72c1a8a511923151124a0dc06b681784dc33515db754e4416b21a07a
-  __DATA_CONST.__mod_term_func: 0x10 sha256:985d4327b559286189b9fa62efc42a04ed2c1a16f16685d5c7cd10e55182905e
-  __DATA_CONST.__const: 0xcb8 sha256:17e0f31c06689732821c193bbbeac3760110dcf711e0a4d7206f7cea9f24c9a2
-  __DATA_CONST.__kalloc_type: 0x80 sha256:fa586489e4695e60af5566c871f426f576ab8cba90ceb463a8083d4860442305
-  UUID: F37B4E44-E908-3625-A1DF-8D735814DF96
-  Functions: 81
+  __DATA_CONST.__mod_init_func: 0x10 sha256:671c9627232c0c73bb3f6d4b43ac5c60ef4414d9b2e228b59887a2605760e4ee
+  __DATA_CONST.__mod_term_func: 0x10 sha256:0fe19773af0d6728ac7d145a32862cb664a8668c64deca49c9e7e13658abf720
+  __DATA_CONST.__const: 0xcb8 sha256:d8277193988bf743b2dd54d7dc8ebb5a2db20b37d552019f97a28bf63b7135b7
+  __DATA_CONST.__kalloc_type: 0x80 sha256:380089b303ca7f30dfc38435f50426bffce8dc45bb2b00addaaabbf715008744
+  __DATA_CONST.__auth_got: 0x100 sha256:8f19363f5417e2627031e01001ad424b31f9b827206dfc4cf0f233662ddb79b9
+  __DATA_CONST.__got: 0x40 sha256:d66d679c2d024bb7289efea76212591732abd3cbcfd07506f95a5dd0463fa3c7
+  UUID: 053E128E-0B3B-3F30-8756-6D91C478900F
+  Functions: 83
   Symbols:   0
-  CStrings:  63
+  CStrings:  65
 
CStrings:
+ "%s%s:\n%s    %scommitting epoch slot %d:%d\n"
+ "%s%s:\n%s    Option \"%s\" disabled by absence in EDT\n"
+ "%s%s:\n%s    Option \"%s\" enabled by presence in EDT\n"
+ "%s%s:\n%s    Option \"%s\" set to %u by boot-arg \"%s\"\n"
+ "12111112122212121221111"
+ "asked to but NOT "
+ "bool AppleEpochManager::_getSandcatOption(DTEntry, const char *)"
+ "bool AppleEpochManager::_updateEpochCommits(SEPEpoch::Epoch *, SEPEpoch::EpochIndex, uint8_t)"
+ "dc_epoch_roll"
+ "factory_key_disable"
+ "len > 0 && (size_t)len < sizeof(bootarg_name)"
+ "nullptr != epoch_array"
+ "nullptr != name"
+ "sandcat_%s"
- "%s%s:\n%s    Epoch processing disabled\n"
- "%s%s:\n%s    Epoch proposal processing enabled by DT\n"
- "%s%s:\n%s    Epoch proposal processing overriden by boot-arg to %u\n"
- "%s%s:\n%s    Found valid berb proposal for slot %d:%d\n"
- "%s%s:\n%s    Found valid epoch proposal for slot %d:%d\n"
- "%s%s:\n%s    Found valid refk proposal for slot %d:%d\n"
- "%s%s:\n%s    epoch processing disabled\n"
- "121111121222121212211211"
- "bool AppleEpochManager::_findEpochProposalProcessingStatus(DTEntry)"
- "epoch-bumps"
- "sandcat_epochs"
- "seeker-ok-to-commit-eply"

```
