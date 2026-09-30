## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-817.0.0.0.0
-  __TEXT.__cstring: 0xab46
+817.40.2.0.0
+  __TEXT.__cstring: 0xb3c2
   __TEXT.__const: 0x28a20
-  __TEXT.__os_log: 0x6e76
-  __TEXT_EXEC.__text: 0x38f7c
+  __TEXT.__os_log: 0x70ad
+  __TEXT_EXEC.__text: 0x3a754
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x450
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__mod_init_func: 0xd8
   __DATA_CONST.__mod_term_func: 0xd8
-  __DATA_CONST.__const: 0x66c8
+  __DATA_CONST.__const: 0x67f8
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: 0CC00A9C-E4A4-37EE-9575-B80F3FA87AB1
-  Functions: 901
+  UUID: B966C373-8FE9-350C-8B04-B4025988B59D
+  Functions: 922
   Symbols:   0
-  CStrings:  927
+  CStrings:  955
 
CStrings:
+ "\"AppleThunderboltHALGenericACIO::determineSIDPartitioning() failed - Invalid ACIO IOMapper count %zu. Expected either a single mapper or %zu mappers for %zu NHI rings.\" @%s:%d"
+ "\"AppleThunderboltNHIGenericACIO::determineSIDPartitioning() failed: HAL provider (%s) Missing iommu-parent in device tree\" @%s:%d"
+ "\"AppleThunderboltNHIGenericACIO::determineSIDPartitioning() failed: Invalid ACIO mapper in device tree. iommu-parent '%s' was of type '%s', not IOMapper or OSData.\" @%s:%d"
+ "\"AppleThunderboltNHIGenericACIO::determineSIDPartitioning() failed: caller passed null provider.\" @%s:%d"
+ "%lldus AppleThunderboltHALGenericACIO::createDeviceMemoryForRange - memory = %p, status = 0x%08x\n"
+ "%lldus AppleThunderboltHALGenericACIO::createDeviceMemoryForRange - range = %d offset = 0x%llx length = 0x%llx\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to create RX mapper for hopID %d, index %d!\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to create TX mapper for hopID %d, index %d!\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: invalid SID partitioning scheme! fDartSIDPartitioning = %d\n"
+ "%lldus AppleThunderboltHALGenericACIO::initializeMappers - done, status = 0x%08x, alignment = 0x%x\n"
+ "%lldus AppleThunderboltHALGenericACIO::poweredStart - fDartSIDPartitioning = 0x%08x\n"
+ "%lldus AppleThunderboltNHIReceiveRing(%d)::unconfigure - fOwner = %p, fSoftInterruptEventSource = %p\n"
+ "%lldus AppleThunderboltNHIReceiveRingManager::deallocateReceiveRing - deallocating Rx ring %p\n"
+ "%lldus AppleThunderboltNHITransmitRingManager::deallocateTransmitRing - deallocating Tx ring %p\n"
+ "121111121222121211221111111111222122112222222211121111111111111111111111111111121211211121112111211121112111212111111111111111111111111212121"
+ "1211111212221212112211111111112221221122222222111211111111111111111111111111111212112111211121112111211121112121111111111111111111111112121211"
+ "1211122222211211112222211221"
+ "12111222222112111122222211212"
+ "1211122222211211112222221121212"
+ "21:17:33"
+ "AppleThunderboltHALGenericACIO.cpp"
+ "OSBoundedPtr.h"
+ "Oct  1 2025"
+ "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally"
+ "iommu-parent"
- "121111121222121211221111111111222122112222222211121111111111111111111111111111121212112112112112112112112121"
- "1211111212221212112211111111112221221122222222111211111111111111111111111111111212121121121121121121121121211"
- "1211122222211211112222221121"
- "121112222221121111222222112112"
- "20:21:17"
- "Sep 16 2025"

```
