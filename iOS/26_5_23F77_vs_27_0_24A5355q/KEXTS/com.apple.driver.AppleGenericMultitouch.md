## com.apple.driver.AppleGenericMultitouch

> `com.apple.driver.AppleGenericMultitouch`

```diff

-26.3.0.0.0
-  __TEXT.__cstring: 0x68aa sha256:012fd6b0710f65a02e4a7e67858315dabe44042dc3b607bab28b2bcb998ddc6c
-  __TEXT.__const: 0x21e sha256:b9560a3e6cd3dc056bde14bdcf190b7d07cc609acc3431bd739d048ae545a7e3
-  __TEXT.__os_log: 0x102f sha256:4df0e0b14a72b6ad493179b7898ddbcfa65ddda81be6ed21a0cd6d74ff58a322
-  __TEXT_EXEC.__text: 0x78c0 sha256:36ba6a43b9034f26450f0ef9da0baf289a113865c19b135cb2997e826f8318e4
+29.0.0.0.0
+  __TEXT.__cstring: 0x6ccc sha256:b969812c3f6144cee4c4ba771a15f55f5324d44930ad562e68d476c712b0d18a
+  __TEXT.__const: 0x236 sha256:08b3febd14db7bc050f639cd8094cfd6df37b79fa9b03a21e6bfdc07b7266cd1
+  __TEXT.__os_log: 0x2ae7 sha256:ea470d91ab414eec9ec30f9424626c230569206fa220a0d504ec68a04b804915
+  __TEXT_EXEC.__text: 0xa280 sha256:04c3debe34620d83952636b97a26c4870d054e5e0dadf2f07861d6f52f8da075
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd4 sha256:a34faa790d7ac92550fc211a40bf6215f06dd98fe1ef7e6fe542320bec53e3f7
-  __DATA.__common: 0x80 sha256:38723a2e5e8a17aa7950dc008209944e898f69a7bd10a23c839d341e935fd5ca
+  __DATA.__data: 0xd4 sha256:4d2176781c11c59708aaf4ea67638f89492e9aa97fbec1bf01866df1f1597b14
+  __DATA.__common: 0xa8 sha256:e3c2af35d1dfc500e16f826a071cc311bf55003a3de77de7ea3376c6b6fa2857
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
-  __DATA_CONST.__auth_got: 0x198 sha256:0bf0b908d76f4eb3468c3797df6272b6a5ac03dd6a0a7e196f34ea989a88f64f
-  __DATA_CONST.__got: 0xb8 sha256:20ea323caca5470f29cb8cb3ab89ec6509139d339d54ba9c0b8cf20da6465fc8
-  __DATA_CONST.__mod_init_func: 0x18 sha256:bea1ee401b0813f6c9828b437ece4af615366220d1514e9d772a0b96dd9ea94e
-  __DATA_CONST.__mod_term_func: 0x18 sha256:c6afb3f87568b8f1918f4d9684c2a54877833608e02c1c61c2df86182b9b5b02
-  __DATA_CONST.__const: 0x1658 sha256:0f2052489897308e843e89203ce88df346d8484d6c36962f207022707fa0dd60
-  __DATA_CONST.__kalloc_type: 0x1c0 sha256:1a792614e6c110eefcc87d9bcc7071e90fadb262f47ffe87ff43999521ed8a63
-  UUID: 5198A8D5-4141-3081-8BEC-26D868FE27E9
-  Functions: 221
+  __DATA_CONST.__mod_init_func: 0x18 sha256:7a67b26167e6a266f4c5838732725c1c7f3316e7472f26b38ffabb617214aa5a
+  __DATA_CONST.__mod_term_func: 0x18 sha256:45798babed043786f8ac788fd76fb97fc8b160967c605a595564d990e4fac4b9
+  __DATA_CONST.__const: 0x1780 sha256:d8c2d10700d8c64a03b710766a3f050ae42835fc939228f34e5e227704ad824e
+  __DATA_CONST.__kalloc_type: 0x200 sha256:ebac41211d37b76cdffa0c65dbb3a9f0f08ba78b25f1bf1ec02b106ce6fa4936
+  __DATA_CONST.__auth_got: 0x1b8 sha256:417ce466faef275913831d993036db14633bbe72ac214a869117ae5d9778266f
+  __DATA_CONST.__got: 0xc8 sha256:67c0f60b379fba21cb03c0aefe7c64f3b29c786cfb3daf7ab6387453e50c3daf
+  UUID: A7BA2DCB-3A2D-3F09-B2BE-CD3D8307DD2C
+  Functions: 244
   Symbols:   0
-  CStrings:  201
+  CStrings:  323
 
CStrings:
+ "%u"
+ "121111121222121211111"
+ "12112111"
+ "AppleGenericMultitouchDeciderHelper"
+ "AppleGenericMultitouchDeciderHelper *AppleGenericMultitouchDecider::findHelperForInterface(UInt32)"
+ "ComponentIndex"
+ "IOReturn AppleGenericMultitouchDeciderHelper::authCPInterest(void *, UInt32, IOService *, void *, vm_size_t)"
+ "[Decider] %s\n%s line %d"
+ "[Decider] All interface states are determined\n%s line %d"
+ "[Decider] All interfaces matched, disabling notifier\n%s line %d"
+ "[Decider] All states determined, processing final decision\n%s line %d"
+ "[Decider] AuthCP service has interface index: %u\n%s line %d"
+ "[Decider] AuthCP service has no interface index, using default 0\n%s line %d"
+ "[Decider] AuthCP service is not a touch controller (flags=0x%08x)\n%s line %d"
+ "[Decider] AuthCP service matched: %s\n%s line %d"
+ "[Decider] Boot args check complete: all states determined = %u\n%s line %d"
+ "[Decider] Boot args not set, setting up matching callback\n%s line %d"
+ "[Decider] Cannot find helper - helpers array is null\n%s line %d"
+ "[Decider] Cannot get interface name - mappings not initialized\n%s line %d"
+ "[Decider] Checking boot args for all helpers\n%s line %d"
+ "[Decider] Checking if all %u interface(s) have states determined\n%s line %d"
+ "[Decider] Cleaning up %u helper(s)\n%s line %d"
+ "[Decider] Couldn't cast flagsObj!\n%s line %d"
+ "[Decider] Couldn't get flags property!\n%s line %d"
+ "[Decider] Couldn't retrieve class to launch\n%s line %d"
+ "[Decider] Created %u helper(s) with index mappings\n%s line %d"
+ "[Decider] Created helper for index %u (interface: %s, %s mode)\n%s line %d"
+ "[Decider] Creating decider helpers\n%s line %d"
+ "[Decider] Creating helpers\n%s line %d"
+ "[Decider] Disabling authCP match notifier\n%s line %d"
+ "[Decider] Failed start\n%s line %d"
+ "[Decider] Failed to allocate class %s\n%s line %d"
+ "[Decider] Failed to allocate helper for index %u\n%s line %d"
+ "[Decider] Failed to attach %s\n%s line %d"
+ "[Decider] Failed to copy kAppleAuthCPInterfaceIndexKey property from this instance of AppleAuthCPRelay\n%s line %d"
+ "[Decider] Failed to create decider helpers\n%s line %d"
+ "[Decider] Failed to create interface name string for index %u\n%s line %d"
+ "[Decider] Failed to create key symbol for index %u\n%s line %d"
+ "[Decider] Failed to init %s\n%s line %d"
+ "[Decider] Failed to initialize helper for index %u\n%s line %d"
+ "[Decider] Failed to parse AuthSourceIndex for interface %s, using legacy mode\n%s line %d"
+ "[Decider] Failed to process child\n%s line %d"
+ "[Decider] Failed to process config provider\n%s line %d"
+ "[Decider] Failed to set up AuthCP matching callback\n%s line %d"
+ "[Decider] Failed to start %s\n%s line %d"
+ "[Decider] Finding AID image downloaders\n%s line %d"
+ "[Decider] Found %u AID image downloaders\n%s line %d"
+ "[Decider] Found auth-required child: %s\n%s line %d"
+ "[Decider] Found auth-required on config provider: %s\n%s line %d"
+ "[Decider] Found helper for interface index %u\n%s line %d"
+ "[Decider] Found touch instance of AppleAuthCPRelay\n%s line %d"
+ "[Decider] Helper for interface %u still waiting for AuthCP service\n%s line %d"
+ "[Decider] Helper state changed callback for interface %u\n%s line %d"
+ "[Decider] Interface %s uses legacy auth (no AuthSourceIndex), defaulting to index 0\n%s line %d"
+ "[Decider] Interface %s uses multi-interface auth with index %u\n%s line %d"
+ "[Decider] Interface %u is not authentic in multi-interface device\n%s line %d"
+ "[Decider] Interface %u states not ready (auth=%u, trust=%u)\n%s line %d"
+ "[Decider] Interface 0 is %s\n%s line %d"
+ "[Decider] Launch %s\n%s line %d"
+ "[Decider] Launching %s\n%s line %d"
+ "[Decider] Launching IOService: %s\n%s line %d"
+ "[Decider] Legacy mode detected, config provider is the only interface\n%s line %d"
+ "[Decider] Legacy mode detected, stopping search after first interface\n%s line %d"
+ "[Decider] Maximum string size exceeded\n%s line %d"
+ "[Decider] Multi-interface mode with %u interfaces\n%s line %d"
+ "[Decider] Multi-interface overall authentic state: %u\n%s line %d"
+ "[Decider] No auth-required entries found\n%s line %d"
+ "[Decider] No helper found for interface index %u\n%s line %d"
+ "[Decider] No helpers available to check states\n%s line %d"
+ "[Decider] No helpers pointer, or helpers count = 0\n%s line %d"
+ "[Decider] No interface name found for index %u\n%s line %d"
+ "[Decider] Processing all states ready - making final launch decision\n%s line %d"
+ "[Decider] Processing state change for interface %u (authDetermined=%u, trustDetermined=%u)\n%s line %d"
+ "[Decider] Recorded start begin time\n%s line %d"
+ "[Decider] Recording ultimate decision: authentic=%u, launchSuccess=%u\n%s line %d"
+ "[Decider] Searching for entries with auth-required property\n%s line %d"
+ "[Decider] Searching parent, name: %s\n%s line %d"
+ "[Decider] Setting up AuthCP matching callback\n%s line %d"
+ "[Decider] Single interface mode\n%s line %d"
+ "[Decider] Starting AppleGenericMultitouchDecider\n%s line %d"
+ "[Decider] Stopped AppleGenericMultitouchDecider\n%s line %d"
+ "[Decider] Stopping AppleGenericMultitouchDecider\n%s line %d"
+ "[Decider] Successfully set up AuthCP matching callback\n%s line %d"
+ "[Decider] Successfully started AppleGenericMultitouchDecider\n%s line %d"
+ "[Decider] Ultimate decision recorded: %u\n%s line %d"
+ "[Decider] Using config provider: %s\n%s line %d"
+ "[Decider] Waiting for more states to be determined\n%s line %d"
+ "[Decider] flags = 0x%08x\n%s line %d"
+ "[Decider] helperStateChanged called with null helper\n%s line %d"
+ "[Helper %u] Checking boot args for interface %u\n%s line %d"
+ "[Helper %u] Duplicate authenticity state determined for interface %u, ignoring\n%s line %d"
+ "[Helper %u] Duplicate trust state determined for interface %u, ignoring\n%s line %d"
+ "[Helper %u] Freeing helper for interface %u\n%s line %d"
+ "[Helper %u] Initializing helper for interface %u\n%s line %d"
+ "[Helper %u] Interface %u authenticity determined: %s\n%s line %d"
+ "[Helper %u] Interface %u received authCP interest callback, messageType=0x%x, argSize=%zu\n%s line %d"
+ "[Helper %u] Interface %u received authenticity callback: %u\n%s line %d"
+ "[Helper %u] Interface %u received trust callback: %u\n%s line %d"
+ "[Helper %u] Interface %u received unhandled message type 0x%x\n%s line %d"
+ "[Helper %u] Interface %u trust determined: %s\n%s line %d"
+ "[Helper %u] Interface %u: %s property exists but is not OSBoolean\n%s line %d"
+ "[Helper %u] Interface %u: %s property not yet available\n%s line %d"
+ "[Helper %u] Interface %u: All states ready, disabling interest notifier\n%s line %d"
+ "[Helper %u] Interface %u: Appending hid-merge-personality with non-auth-suffix: %s\n%s line %d"
+ "[Helper %u] Interface %u: Device not authentic, processing personality override\n%s line %d"
+ "[Helper %u] Interface %u: Failed to process states ready\n%s line %d"
+ "[Helper %u] Interface %u: Found boot arg agm-authentic=%u\n%s line %d"
+ "[Helper %u] Interface %u: Found boot arg agm-trusted=%u\n%s line %d"
+ "[Helper %u] Interface %u: No non-auth-personality or non-auth-suffix found\n%s line %d"
+ "[Helper %u] Interface %u: Overwriting hid-merge-personality with non-auth-personality: %s\n%s line %d"
+ "[Helper %u] Interface %u: Removing eeprom-property (authentic=%u, trusted=%u)\n%s line %d"
+ "[Helper %u] Interface %u: Successfully processed states ready\n%s line %d"
+ "[Helper %u] No auth consumer for interface %u\n%s line %d"
+ "[Helper %u] Polled %s state: %u\n%s line %d"
+ "[Helper %u] Processing states ready for interface %u (authentic=%u, trusted=%u)\n%s line %d"
+ "[Helper %u] Received authCP interest from unexpected service for interface %u\n%s line %d"
+ "[Helper %u] Registered interest notifier for interface %u\n%s line %d"
+ "[Helper %u] Setting AuthCP service for interface %u\n%s line %d"
+ "[Helper %u] Successfully initialized helper for interface %u\n%s line %d"
+ "[Helper %u] super::init() failed for interface %u\n%s line %d"
+ "auth-source-index"
+ "authentic"
+ "auto AppleGenericMultitouchDecider::createDeciderHelpers()::(anonymous class)::operator()(IORegistryEntry *) const"
+ "auto AppleGenericMultitouchDecider::start(IOService *)::(anonymous class)::operator()(AppleGenericMultitouchDecider *) const"
+ "bool AppleGenericMultitouchDecider::areAllStatesDetermined()"
+ "bool AppleGenericMultitouchDecider::createDeciderHelpers()"
+ "bool AppleGenericMultitouchDeciderHelper::init(StateChangedCallback, void *, UInt32, IORegistryEntry *)"
+ "bool AppleGenericMultitouchDeciderHelper::processStatesReady()"
+ "bool appendStringToDataProperty(IORegistryEntry *, const char *, const char *)"
+ "const char *AppleGenericMultitouchDecider::getInterfaceNameForIndex(UInt32)"
+ "createDeciderHelpers()"
+ "failed"
+ "firstHelper"
+ "helpers"
+ "helpers->getCount() > 0"
+ "legacy"
+ "mappings"
+ "multi-interface"
+ "not authentic"
+ "not trusted"
+ "result != Failed"
+ "site.AppleGenericMultitouchDeciderHelper"
+ "static void AppleGenericMultitouchDecider::helperStateChangedCallback(AppleGenericMultitouchDeciderHelper *, void *)"
+ "succeeded"
+ "trusted"
+ "virtual void AppleGenericMultitouchDecider::stop(IOService *)"
+ "virtual void AppleGenericMultitouchDeciderHelper::free()"
+ "void AppleGenericMultitouchDecider::helperStateChanged(AppleGenericMultitouchDeciderHelper *)"
+ "void AppleGenericMultitouchDecider::processAllStatesReady()"
+ "void AppleGenericMultitouchDeciderHelper::authenticityStateDetermined(bool)"
+ "void AppleGenericMultitouchDeciderHelper::checkBootArgs()"
+ "void AppleGenericMultitouchDeciderHelper::setAuthCPService(IOService *)"
+ "void AppleGenericMultitouchDeciderHelper::trustStateDetermined(bool)"
- "%s\n%s line %d"
- "121111121222121211112"
- "AuthDecisionMade"
- "Couldn't cast flagsObj!\n%s line %d"
- "Couldn't get flags property!\n%s line %d"
- "Couldn't retrieve class to launch\n%s line %d"
- "Duplicate authenticity state determined, ignoring\n%s line %d"
- "Duplicate trust state determined, ignoring\n%s line %d"
- "Failed start\n%s line %d"
- "Found touch instance of AppleAuthCPRelay\n%s line %d"
- "IOReturn AppleGenericMultitouchDecider::authCPInterest(void *, UInt32, IOService *, void *, vm_size_t)"
- "Launching %s\n%s line %d"
- "Maximum string size exceeded\n%s line %d"
- "Polled %s state: %u\n%s line %d"
- "Received callback for authenticity state: %u\n%s line %d"
- "Received callback for trust state: %u\n%s line %d"
- "Searching parent, name: %s\n%s line %d"
- "TrustDecisionMade"
- "Using config provider: %s\n%s line %d"
- "action"
- "auto AppleGenericMultitouchDecider::modifyPersonalities()::(anonymous class)::operator()(IORegistryEntry *, void *) const"
- "bool AppleGenericMultitouchDecider::performActionOnAuthConsumers(AuthConsumerAction *, void *, bool)"
- "bool AppleGenericMultitouchDecider::pollState(IOService *, const char *, bool *)"
- "flags = 0x%08x\n%s line %d"
- "isAuthenticBool"
- "isTrustedBool"
- "stateBool"
- "static bool AppleGenericMultitouchDecider::appendStringToDataProperty(IORegistryEntry *, const char *, const char *)"
- "void AppleGenericMultitouchDecider::authenticityStateDetermined(bool)"
- "void AppleGenericMultitouchDecider::newStateDetermined()"
- "void AppleGenericMultitouchDecider::trustStateDetermined(bool)"

```
