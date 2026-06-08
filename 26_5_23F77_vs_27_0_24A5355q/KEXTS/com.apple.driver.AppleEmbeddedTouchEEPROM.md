## com.apple.driver.AppleEmbeddedTouchEEPROM

> `com.apple.driver.AppleEmbeddedTouchEEPROM`

```diff

-50.120.2.0.0
-  __TEXT.__cstring: 0x96d sha256:064c649846acc87388dac06e089eed76c002218ef67f1eaa5539a321d253eb56
-  __TEXT_EXEC.__text: 0x18a0 sha256:02c3fd37ec0b6ae3728b22cd86d3f6e37f8f738161ec94c80cbed48266c4128e
+55.0.0.0.0
+  __TEXT.__cstring: 0x1fca sha256:c47b3827896ae1582a930007ac7e1fef4358672bddf73bb599d18a9bcb7c3cd0
+  __TEXT_EXEC.__text: 0x3840 sha256:b93b7175b357106eb3450d3ed423134b5b6b71bb637f02c12d144cd9a6359252
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:dc28979fd44e253fa219f1a7931c2928da8f27fd2fd13106b60c355b9de64079
-  __DATA.__common: 0x84 sha256:115bad14f1c9f2c027a84de21b107015722cb76be8d0abf3760ad8e00d6c24a5
-  __DATA_CONST.__auth_got: 0x80 sha256:90805ac49c9b9e3f0c1a2d7f332db08ab989ee44a48a757a422290a8ed1baa7a
-  __DATA_CONST.__got: 0x40 sha256:03130d0ac3e6c085c8fcb65076e955f2985a2846a64a21b4c57520b584f3aea2
-  __DATA_CONST.__mod_init_func: 0x10 sha256:70c04acfb2f80fcc34a8670e04f30685710c5d44fec6c6785116694cc95b7988
-  __DATA_CONST.__mod_term_func: 0x10 sha256:4bbd8d3b7fd5b165213b2116f0f0d8d0c298656af4f7ff31908d68592d1d444d
-  __DATA_CONST.__const: 0xcb8 sha256:a31f1a64c5614c3d53091301d4a553b17655c0c7ed8b495f653a5fae319233de
-  __DATA_CONST.__kalloc_type: 0x80 sha256:f054f01a8f9a52ca489c8a81c518c6cea57993e1a1ba58d39f7d11dfdafea351
-  UUID: B3E448EB-66E7-35F0-890B-5CA06FB53CC8
-  Functions: 57
+  __DATA.__data: 0xc4 sha256:0ce19b5849cb511908476812e86262bd52857dbcfcd416d9afe8093ce09a193f
+  __DATA.__common: 0x3f8 sha256:5817bc65840cf706e658b883fc8a08c91551deb915ac9f5844e0cf807cf0b705
+  __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+  __DATA_CONST.__mod_init_func: 0x10 sha256:1051aa71cd6a3de13dc8938e80b3da0adc635da6a540001b6e21550e256e8a68
+  __DATA_CONST.__mod_term_func: 0x10 sha256:7971850294bc05dad22f44fddc43010a3fe3e838a5b32e9a011da67f5bc2ab45
+  __DATA_CONST.__const: 0xd48 sha256:2bcf99717823048ed378b41886e1cc17a359f02df900e595cea9f249d39895a9
+  __DATA_CONST.__kalloc_type: 0x80 sha256:f2acaa936e2a9970592a8db77663d0c8196b9c6f68348cd36a1807d43ea0e1d8
+  __DATA_CONST.__auth_got: 0xd0 sha256:d1ec986c12dde827ffcc499960f11eaca3a389863ffff2363fc4733115ea3793
+  __DATA_CONST.__got: 0x48 sha256:5d4b7be003f67bfc1d03e485164b1f781d377b1877d28fe17dd755b66574a5dc
+  UUID: 04477B22-641F-3E5B-BC2E-56C95CED921B
+  Functions: 72
   Symbols:   0
-  CStrings:  48
+  CStrings:  143
 
CStrings:
+ "%u"
+ "12111112122212121"
+ "EEPROMGetInstanceCount"
+ "EEPROMGetInstanceIndexByName"
+ "EEPROMGetInstanceNameByIndex"
+ "EEPROMGetRegionSize"
+ "EEPROMGetRegionSizeOfInstance"
+ "EEPROMRead"
+ "EEPROMReadFromInstance"
+ "EEPROMWrite"
+ "EEPROMWriteToInstance"
+ "TouchEEPROMDriver::%s: Added new EEPROM instance %u for NOR device %p (device: %s)\n\n"
+ "TouchEEPROMDriver::%s: AppleEmbeddedTouchEEPROMDriver class instance not found\n\n"
+ "TouchEEPROMDriver::%s: Bad input count: %u\n\n"
+ "TouchEEPROMDriver::%s: Buffer size is smaller than expected. Expected size is %u. Buffer Size received is %u\n\n"
+ "TouchEEPROMDriver::%s: Cannot extract region sizes from EDT for service %s\n\n"
+ "TouchEEPROMDriver::%s: Device '%s' assigned to target instance ID %u (name-based fallback)\n\n"
+ "TouchEEPROMDriver::%s: Device '%s' not found\n\n"
+ "TouchEEPROMDriver::%s: Device name is NULL, cannot register EEPROM instance\n\n"
+ "TouchEEPROMDriver::%s: EEPROM %u (%s) Read from offset = 0x%08x, size = 0x%08x \n"
+ "TouchEEPROMDriver::%s: EEPROM %u (%s) Write to offset = 0x%08x, size = 0x%08x \n"
+ "TouchEEPROMDriver::%s: EEPROM %u Size for region regionType: %x is %u\n\n"
+ "TouchEEPROMDriver::%s: EEPROM %u name is %s\n\n"
+ "TouchEEPROMDriver::%s: EEPROM instance already exists with index %u\n\n"
+ "TouchEEPROMDriver::%s: EEPROM valid instance count is %u (array size: %u)\n\n"
+ "TouchEEPROMDriver::%s: Failed to add EEPROM instance for NOR device %p (%s) - maximum instances (%u) reached or other error. EEPROM discovered but not accessible to userspace.\n\n"
+ "TouchEEPROMDriver::%s: Found NOR device %p for service %p\n\n"
+ "TouchEEPROMDriver::%s: Found device '%s' at instance %u\n\n"
+ "TouchEEPROMDriver::%s: Found display-index property: %u\n\n"
+ "TouchEEPROMDriver::%s: Grandparent service found but no name property, using fallback service name\n\n"
+ "TouchEEPROMDriver::%s: IOService not found\n\n"
+ "TouchEEPROMDriver::%s: Invalid EEPROM Instance: %u (array size: %u, device: %p)\n\n"
+ "TouchEEPROMDriver::%s: Invalid EEPROM device name: deviceName = %p, length = %u\n"
+ "TouchEEPROMDriver::%s: Invalid buffer: buffer = %p, size = %u\n"
+ "TouchEEPROMDriver::%s: Invalid device name format '%s', using fallback instance %u\n\n"
+ "TouchEEPROMDriver::%s: Invalid name buffer\n\n"
+ "TouchEEPROMDriver::%s: Invalid parameters\n\n"
+ "TouchEEPROMDriver::%s: Invalid region regionType: %u\n\n"
+ "TouchEEPROMDriver::%s: Invalid regionType: %u\n\n"
+ "TouchEEPROMDriver::%s: Maximum EEPROM instances (%u) reached\n\n"
+ "TouchEEPROMDriver::%s: No grandparent service found, using fallback service name\n\n"
+ "TouchEEPROMDriver::%s: No parent service found, using fallback service name\n\n"
+ "TouchEEPROMDriver::%s: No valid display-index property found, using name-based fallback\n\n"
+ "TouchEEPROMDriver::%s: Null buffer\n\n"
+ "TouchEEPROMDriver::%s: Null pointer\n"
+ "TouchEEPROMDriver::%s: Null pointer for count\n\n"
+ "TouchEEPROMDriver::%s: Null pointer for size\n\n"
+ "TouchEEPROMDriver::%s: Null pointer to size\n\n"
+ "TouchEEPROMDriver::%s: Null pointer: target = %p arguments = %p\n"
+ "TouchEEPROMDriver::%s: Null pointer: target = %p reference = %p arguments = %p\n"
+ "TouchEEPROMDriver::%s: Number of BIM regions returned from EDT does not match the expected count. Got %lu, expected %d\n\n"
+ "TouchEEPROMDriver::%s: Service %p (class: %s) is not an AppleARMNORFlashDevice\n\n"
+ "TouchEEPROMDriver::%s: Service name is '%s' (length=%u)\n\n"
+ "TouchEEPROMDriver::%s: Set EEPROM %u name to %s\n\n"
+ "TouchEEPROMDriver::%s: Setting up %lu regions for EEPROM %u (%s)\n\n"
+ "TouchEEPROMDriver::%s: Target instance ID %u exceeds maximum (%u)\n\n"
+ "TouchEEPROMDriver::%s: Target instance ID %u is already occupied by device '%s'\n\n"
+ "TouchEEPROMDriver::%s: Unknown device name pattern '%s', using fallback instance %u\n\n"
+ "TouchEEPROMDriver::%s: Using display-index property value %u for instance ID\n\n"
+ "TouchEEPROMDriver::%s: Using grandparent device name '%s' (I2C device, length=%u)\n\n"
+ "TouchEEPROMDriver::%s: [ENTRY] AppleEmbeddedTouchEEPROMDriver::start() called with provider=%p\n"
+ "TouchEEPROMDriver::%s: [ENTRY] UserClient start called with provider=%p\n"
+ "TouchEEPROMDriver::%s: [ENTRY] externalMethod called with selector=%u\n"
+ "TouchEEPROMDriver::%s: [ENTRY] getRegionSizeInternal called\n"
+ "TouchEEPROMDriver::%s: [ENTRY] initWithTask called with owningTask=%p, type=%u\n"
+ "TouchEEPROMDriver::%s: [ENTRY] publishNotificationHandler called\n"
+ "TouchEEPROMDriver::%s: [ENTRY] readRegion called with eepromInstanceID=%u, regionType=%u, buffer=%p, outSize=%p\n"
+ "TouchEEPROMDriver::%s: [ENTRY] readRegionInternal called\n"
+ "TouchEEPROMDriver::%s: [ENTRY] writeRegion called with eepromInstanceID=%u, regionType=%u, buffer=%p, inSize=%u\n"
+ "TouchEEPROMDriver::%s: [ENTRY] writeRegionInternal called\n"
+ "TouchEEPROMDriver::%s: [ERROR] Actual region count (%u) does not match expected region count (%u)\n"
+ "TouchEEPROMDriver::%s: [ERROR] Failed to allocate EEPROM lock.\n"
+ "TouchEEPROMDriver::%s: [ERROR] Failed to cast provider to AppleEmbeddedTouchEEPROMDriver\n"
+ "TouchEEPROMDriver::%s: [ERROR] Failed to get entitlement object\n"
+ "TouchEEPROMDriver::%s: [ERROR] Invalid selector: %u (max: %u)\n"
+ "TouchEEPROMDriver::%s: [ERROR] Start failing in the provider.\n"
+ "TouchEEPROMDriver::%s: [ERROR] addMatchingNotification() failed\n"
+ "TouchEEPROMDriver::%s: [ERROR] owningTask is null\n"
+ "TouchEEPROMDriver::%s: [ERROR] provider is not a NOR flash device.\n"
+ "TouchEEPROMDriver::%s: [EXIT] AppleEmbeddedTouchEEPROMDriver::start() completed successfully\n"
+ "TouchEEPROMDriver::%s: [EXIT] UserClient start returning: %s\n"
+ "TouchEEPROMDriver::%s: [EXIT] externalMethod returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [EXIT] getRegionSizeInternal returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [EXIT] initWithTask returning: %s\n"
+ "TouchEEPROMDriver::%s: [EXIT] publishNotificationHandler completed successfully for EEPROM %u\n"
+ "TouchEEPROMDriver::%s: [EXIT] readRegion returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [EXIT] readRegionInternal returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [EXIT] writeRegion returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [EXIT] writeRegionInternal returning: 0x%x\n"
+ "TouchEEPROMDriver::%s: [INFO] Allocating EEPROM lock for first time\n"
+ "TouchEEPROMDriver::%s: [INFO] Calling target->readRegion with eepromInstanceID=%u, regionType=%u, outSize=%u\n"
+ "TouchEEPROMDriver::%s: [INFO] Calling target->writeRegion with eepromInstanceID=%u, regionType=%u, size=%u\n"
+ "TouchEEPROMDriver::%s: [INFO] Creating new global notification for 'display-generic-data,rw'\n"
+ "TouchEEPROMDriver::%s: [INFO] Direct buffer: %p, size: %u\n"
+ "TouchEEPROMDriver::%s: [INFO] Direct output buffer: %p, size: %u\n"
+ "TouchEEPROMDriver::%s: [INFO] EEPROM lock already exists\n"
+ "TouchEEPROMDriver::%s: [INFO] Getting region size for eepromInstanceID= %u, regionType= 0x%08x\n"
+ "TouchEEPROMDriver::%s: [INFO] Global notificaiton already setup\n"
+ "TouchEEPROMDriver::%s: [INFO] Mapped buffer: %p, size: %u\n"
+ "TouchEEPROMDriver::%s: [INFO] Mapped output buffer: %p, size: %u\n"
+ "TouchEEPROMDriver::%s: [INFO] Read operation for eepromInstanceID= %u, regionType= 0x%08x\n"
+ "TouchEEPROMDriver::%s: [INFO] getRegionSize returned: 0x%x, size=%u\n"
+ "TouchEEPROMDriver::%s: [INFO] readRegion returned: 0x%x, actual size read: %u\n"
+ "TouchEEPROMDriver::%s: [INFO] writeRegion returned: 0x%x\n"
+ "TouchEEPROMDriver::%s: [SUCCESS] Global notification setup successful, handler set to instance %p\n"
+ "TouchEEPROMDriver::%s: display-index value %u exceeds maximum, using fallback\n\n"
+ "TouchEEPROMDriver::%s: map is null.\n"
+ "display-eeprom"
+ "display-eeprom-"
+ "display-index"
+ "externalMethod"
+ "false"
+ "getEEPROMInstanceCount"
+ "getEEPROMInstanceIndexByName"
+ "getEEPROMInstanceNameByIndex"
+ "getRegionSize"
+ "getRegionSizeInternal"
+ "initWithTask"
+ "name"
+ "publishNotificationHandler"
+ "readRegion"
+ "readRegionInternal"
+ "registerEEPROMInstance"
+ "true"
+ "unknown"
+ "validateRegionParameters"
+ "writeRegion"
+ "writeRegionInternal"
- "\n"
- "%s - [ERROR] Actual region count (%u) does not match expected region count (%u)"
- "%s - [ERROR] Start failing in the provider."
- "%s - [ERROR] addMatchingNotification() failed"
- "%s - [ERROR] provider is not a NOR flash device."
- "%s: Bad input count: %u\n"
- "%s: Buffer size is smaller than expected. Expected size is %u.               Buffer Size received is %u\n"
- "%s: IOService not found\n"
- "%s: Invalid type: %u\n"
- "%s: Null pointer or zero-length: buffer = %p"
- "%s: Null pointer: buffer = %p"
- "%s: Null pointer: target = %p reference = %p arguments = %p"
- "%s: Read from offset = 0x%08x, size = 0x%08x "
- "%s: Size for region type: %x is %u\n"
- "%s: Write to offset = 0x%08x, size = 0x%08x "
- "%s: map is null."
- "%s: type= 0x%08x \n"
- "%s:Invalid type: %u\n"
- "%s:Null buffer\n"
- "%s:Null buffer/pointer to size\n"
- "%s:Null pointer for size\n"
- "1211111212221212112"
- "AppleEmbeddedTouchEEPROMDriver class instance not found\n"
- "Cannot extract region sizes from EDT\n"
- "IOReturn AppleEmbeddedTouchEEPROMDriver::getRegionSize(uint8_t, uint32_t *)"
- "IOReturn AppleEmbeddedTouchEEPROMDriver::readRegion(uint8_t, const uint8_t *, uint32_t *)"
- "IOReturn AppleEmbeddedTouchEEPROMDriver::writeRegion(uint8_t, const uint8_t *, uint32_t)"
- "Number of BIM regions returned from EDT does not match the expected count\n"
- "Number of regions returned from EDT is %lu\n"
- "static IOReturn AppleEmbeddedTouchEEPROMDriverUC::EEPROMGetRegionSize(AppleEmbeddedTouchEEPROMDriver *, void *, IOExternalMethodArguments *)"
- "static IOReturn AppleEmbeddedTouchEEPROMDriverUC::EEPROMRead(AppleEmbeddedTouchEEPROMDriver *, void *, IOExternalMethodArguments *)"
- "static IOReturn AppleEmbeddedTouchEEPROMDriverUC::EEPROMWrite(AppleEmbeddedTouchEEPROMDriver *, void *, IOExternalMethodArguments *)"
- "static bool AppleEmbeddedTouchEEPROMDriver::publishNotificationHandler(AppleEmbeddedTouchEEPROMDriver *, void *, IOService *)"

```
