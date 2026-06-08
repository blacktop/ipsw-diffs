## com.apple.driver.AppleEpochManager

> `com.apple.driver.AppleEpochManager`

```diff

-11.0.0.0.0
-  __TEXT.__cstring: 0x93a
+14.0.0.0.0
+  __TEXT.__cstring: 0x953
   __TEXT.__const: 0x38
-  __TEXT_EXEC.__text: 0x1aec
+  __TEXT_EXEC.__text: 0x1aa8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: F37B4E44-E908-3625-A1DF-8D735814DF96
-  Functions: 81
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x40
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
