## KDKs

- `KDK_26.0_25A5327h.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_26.0_25A5338b.kdk/System/Library/Kernels/kernel.release.t6031`

#### __block_literal_10

```diff

  bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 class IOUserServer* this;	
+class OSArray* services;	
 IOOptionBits terminateFlags;	
 }

```
