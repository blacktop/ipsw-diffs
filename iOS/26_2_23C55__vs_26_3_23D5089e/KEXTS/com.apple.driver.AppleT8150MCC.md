## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

```diff

-78.60.2.0.0
-  __TEXT.__cstring: 0x52fe
-  __TEXT.__os_log: 0x21c5
+78.80.7.0.0
+  __TEXT.__cstring: 0x548e
+  __TEXT.__os_log: 0x2259
   __TEXT.__const: 0x48
-  __TEXT_EXEC.__text: 0x157ec
+  __TEXT_EXEC.__text: 0x15acc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x8b70
   __DATA.__common: 0x1c8

   __DATA_CONST.__const: 0x30d0
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: DFC8B1B3-3A1D-3548-8989-5283545ABB74
-  Functions: 512
+  UUID: 27AD581C-D28C-30A1-B220-4AE7116B9A8F
+  Functions: 514
   Symbols:   0
-  CStrings:  858
+  CStrings:  867
 
CStrings:
+ "\"%s: \" \"SoCNI count %d is greater than number of SoCNI apertures(%d)\" @%s:%d"
+ "\"%s: \" \"Total AMCC Count %d exceeds the max value that the _amccEnbaleMask can represent\" @%s:%d"
+ "\"%s: \" \"_socniApertureCnt %d exceeds the max value _socniEnableMask can represent\" @%s:%d"
+ "%s:%d: _dieNum = %d _amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d\n"
+ "%s:%d: die-enable-mask is not set in EDT. Setting it to 0x%x\n\n"
+ "%s:%d: die-enable-mask: 0x%x\n\n"
+ "%s:%d: regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%x\n"
+ "1211111212221212111111111111111111111111121111111111111111111111111111111111111111111111111111111111111111111211111112121111121112222222222221111111211111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211212121212"
+ "_dieNum = %d _amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d"
+ "die-enable-mask"
+ "die-enable-mask is not set in EDT. Setting it to 0x%x\n"
+ "die-enable-mask: 0x%x\n"
+ "regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%x"
- "\"%s: \" \"SocNI count %d is greater than number of SoCNI apertures(%d)\" @%s:%d"
- "%s:%d: _amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d\n"
- "121111121222121211111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111121111111212111112111222222222221111111211111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211212121212"
- "_amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d"

```
