## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

```diff

-1310.13.0.0.0
-  __TEXT.__os_log: 0x4257
+1310.14.0.0.0
+  __TEXT.__os_log: 0x4259
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x2050
-  __TEXT_EXEC.__text: 0x28e24
+  __TEXT_EXEC.__text: 0x28e6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: D45F88D3-029B-333F-B98A-0094BB267B32
+  UUID: 759A1193-5357-3DA0-92E5-B72DCFF01DF6
   Functions: 877
   Symbols:   0
   CStrings:  657
Functions:
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString -> __Z34corecaptureIsDevFusedOrCSRInternalb : 100 -> 120
~ sub_fffffe000afd274c -> sub_fffffe000b0d30d0 : 116 -> 100
~ __ZN6CCPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 7152 -> 7192
~ __Z16DefaultLogPolicyv : 108 -> 100
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 192 -> 196
~ __ZN16CCPipeUserClient12initWithTaskEP4taskPvjP12OSDictionary : 368 -> 372
~ sub_fffffe000afda858 -> sub_fffffe000b0db1f4 : 8 -> 12
~ sub_fffffe000afe26bc -> sub_fffffe000b0e305c : 188 -> 192
~ sub_fffffe000afee500 -> sub_fffffe000b0eeea4 : 984 -> 996
~ __ZN9CCLogPipe16reserveRingEntryEmjPi : 1624 -> 1628
~ sub_fffffe000aff3a5c -> sub_fffffe000b0f4410 : 96 -> 100
CStrings:
+ "CCLogPipe::log - Required size (%zu) is greater than max (%zu)\n"
- "CCLogPipe::log - Required size (%u) is greater than max (%u)\n"

```
