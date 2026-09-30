## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-817.60.1.0.0
-  __TEXT.__cstring: 0xb3c2
+817.60.2.0.0
+  __TEXT.__cstring: 0xbc66
   __TEXT.__const: 0x28a20
-  __TEXT.__os_log: 0x70ad
-  __TEXT_EXEC.__text: 0x3a754
+  __TEXT.__os_log: 0x7273
+  __TEXT_EXEC.__text: 0x3bbfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
-  __DATA.__common: 0x450
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__mod_init_func: 0xd8
-  __DATA_CONST.__mod_term_func: 0xd8
-  __DATA_CONST.__const: 0x67f8
-  __DATA_CONST.__kalloc_type: 0x6c0
+  __DATA.__common: 0x478
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__mod_init_func: 0xe0
+  __DATA_CONST.__mod_term_func: 0xe0
+  __DATA_CONST.__const: 0x69a8
+  __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: 9F6A8235-0C9A-338F-9838-F68A6410B8DE
-  Functions: 922
+  UUID: 3DECEB5A-6412-3699-AA9E-C1CEB5AF16B9
+  Functions: 947
   Symbols:   0
-  CStrings:  955
+  CStrings:  988
 
CStrings:
+ "\"AppleThunderboltNHIDARTVMAllocator::init - slide cannot be non-zero (found %d)\" @%s:%d"
+ "\"REQUIRE fail: %s @ %s:%u:%s: \" @%s:%d"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to set DART allocator for RX hop ID %d\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to set DART allocator for TX hop ID %d\n"
+ "%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR null mapper passed\n"
+ "%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR: failed to create DARTVMAllocator\n"
+ "%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR: failed to set DARTVMAllocator\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::forMapper\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::init\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::init - DART reported minDVA %p and maxDVA %p and page size %p and thus fSupportsFixedAllocations = %d\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric could not fetch DART capability\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric failed to initialize\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: IOMemoryDescriptor asked for a fixed DART offset but did not supply one via setContext\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: IOMemoryDescriptor asked for a fixed DART offset, but fixed DART offsets are not supported on this device\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: cannot make requested allocation at 0x%08x/%d\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: failed to get VM space for allocation at page 0x%08x and DVA %p\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: requested DVA %p not between minDVA %p and maxDVA %p\n"
+ "%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: tailPadding %d not supported when allocating at a specific offset\n"
+ "/Library/Caches/com.apple.xbs/Sources/AppleThunderboltNHI/AppleThunderboltNHIDARTVMAllocator.cpp"
+ "121111111122222"
+ "21:37:24"
+ "22222223312322"
+ "AppleThunderboltNHIDARTVMAllocator"
+ "AppleThunderboltNHIDARTVMAllocator.cpp"
+ "Nov 12 2025"
+ "n && !(n & (n - 1))"
+ "setAllocator"
+ "site.AppleThunderboltNHIDARTVMAllocator"
+ "site.const IODART::capability_t"
+ "uint32_t log2i(uint32_t)"
- "20:46:20"
- "Nov  3 2025"

```
