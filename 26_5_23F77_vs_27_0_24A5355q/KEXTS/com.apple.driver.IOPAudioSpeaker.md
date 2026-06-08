## com.apple.driver.IOPAudioSpeaker

> `com.apple.driver.IOPAudioSpeaker`

```diff

-940.17.0.0.0
+1000.40.0.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x19e
-  __TEXT.__os_log: 0x8b
-  __TEXT_EXEC.__text: 0x15d4
+  __TEXT.__cstring: 0x4c3
+  __TEXT.__os_log: 0x1ae
+  __TEXT_EXEC.__text: 0x2358
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0xb68
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 0A91E341-B180-39F2-A213-6F61F082E0B7
-  Functions: 56
+  __DATA_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x48
+  UUID: 78AC3E92-F03D-3149-A3CA-079F81CFED8C
+  Functions: 65
   Symbols:   0
-  CStrings:  23
+  CStrings:  40
 
CStrings:
+ "\"%s\" @%s:%d"
+ "%s::%s line:%d inDirection:%u"
+ "%s::%s line:%d inDirection:%u outCurrentBitsPerSample=%u ret=%d"
+ "%s::%s() ByteOffset=%d, nodeID %c%c%c%c, propertyID %d edtKeyName:%s\n"
+ "%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n"
+ "%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n\n"
+ "%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n"
+ "%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n\n"
+ "OSBoundedPtr.h"
+ "The offset of the pointer inside its valid memory range can't be represented using int32_t"
+ "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally"
+ "bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow."
+ "device-property-list"
+ "getSupportedBitsPerSampleList"
+ "transferEdtDeviceProperties"

```
