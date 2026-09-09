## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

 511.0.0.0.0
-  __TEXT.__text: 0xc2e78
+  __TEXT.__text: 0xc2ee4
   __TEXT.__objc_methlist: 0xab1c
   __TEXT.__const: 0x718
   __TEXT.__cstring: 0x8da4

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3950
+  Functions: 3951
   Symbols:   9437
   CStrings:  2294
 
Functions:
~ _DNDSRedactSysdiagnose : 88 -> 92
~ -[DNDSSyncEngineMetadataStore recordWithID:].cold.1 : 148 -> 144
~ -[DNDSSyncEngineMetadataStore purge].cold.1 : 64 -> 72
~ -[DNDSSyncEngineMetadataStore _read].cold.1 : 96 -> 92
~ -[DNDSSyncEngineMetadataStore _write].cold.1 : 64 -> 72
+ -[DNDSIDSSyncEngineMetadataStore _read].cold.1
```
