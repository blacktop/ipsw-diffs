## apfs_stats

> `/System/Library/Filesystems/apfs.fs/apfs_stats`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x30e8
-  __TEXT.__auth_stubs: 0x440
+2632.0.15.0.1
+  __TEXT.__text: 0x2444
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x1f0e
+  __TEXT.__cstring: 0x13e3
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA.__bss: 0x29
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: FB9EC610-518B-3BCA-9A2C-765808C098A9
-  Functions: 19
-  Symbols:   81
-  CStrings:  224
+  UUID: A3F6B728-385C-3BF7-8A6D-A65EAF2EA448
+  Functions: 18
+  Symbols:   78
+  CStrings:  150
 
Symbols:
- _CFRetain
- _IORegistryEntryGetParentIterator
- _putchar
CStrings:
+ "\tContainer: size %lld blocks, %lld blocks free\n"
+ "APFSContainer: %s\n"
- "\tCapacity tier%s%s: size %lld blocks, %lld blocks free\n"
- "\tMain tier%s%s: size %lld blocks, %lld blocks free\n"
- " on "
- "%s                        %u active;    Reads: %u, Writes: %u (WBC: %u, RCWr: %u, bypassed %u)\n"
- "%s                        %u blocked (total so far %u)\n"
- "%s                        %u completed WBC writes (max %u)\n"
- "%s                        %u free (min %u)\n"
- "%s                        %u total accounted\n"
- "%s                   Max: %llu MiB (%llu blocks) %.2f%%\n"
- "%s                  Free: %llu MiB (%llu blocks) %.2f%%\n"
- "%s             Meta:      %llu MiB (%llu blocks) %.2f%%\n"
- "%s!!!!WARNING!!!! HDD is smaller than SSD, an upside-down Fusion?\n"
- "%sAPFS Fusion container stats:\n"
- "%sAllocated by RC:        %llu MiB (%llu blocks) %.2f%%\n"
- "%sAvailable for promoter: %llu MiB (%llu blocks) %.2f%%\n"
- "%sBytes elevated so far:  %llu MiB (%llu blocks)\n"
- "%sBytes written into WBC: %llu MiB\n"
- "%sCurrent offset    Head: %llu Tail: %llu\n"
- "%sDirty in RC:            %llu MiB (%llu blocks) %.2f%%\n"
- "%sElevator Trottled:      %llu times\n"
- "%sHDD available now:      %llu MiB (%llu blocks) %.2f%%\n"
- "%sHDD free total:         %llu MiB (%llu blocks) %.2f%%\n"
- "%sHDD freeQ:              %llu MiB (%llu blocks) %.2f%%\n"
- "%sHDD reserved Data:      %llu MiB (%llu blocks) %.2f%%\n"
- "%sHDD size:               %llu MiB (%llu blocks)\n"
- "%sIs MT synchronized:     %s\n"
- "%sMT btree stats:         %llu records, %llu nodes, %u depth, WS ~%llu KiB maximum\n"
- "%sMT dirtyRC:             %u blocks %i cnt delta\n"
- "%sMT totalRC:             %u blocks %i cnt delta\n"
- "%sMT wbc:                 %u blocks\n"
- "%sProcessed by elevator:  %llu MiB (%llu extents)\n"
- "%sPromoter Trottled:      %llu times\n"
- "%sRC auto promo. mult:    %u\n"
- "%sRC auto promotion:      %s"
- "%sRC fast promote:        %s\n"
- "%sRC lazy promote:        %s\n"
- "%sRevMT btree stats:      %llu records, %llu nodes, %u depth, WS ~%llu KiB current\n"
- "%sSSD available now:      %llu MiB (%llu blocks) %.2f%%\n"
- "%sSSD free total:         %llu MiB (%llu blocks) %.2f%%\n"
- "%sSSD freeQ:              %llu MiB (%llu blocks) %.2f%%\n"
- "%sSSD reserved Data:      %llu MiB (%llu blocks) %.2f%%\n"
- "%sSSD size w/o WBC:       %llu MiB (%llu blocks)\n"
- "%sSpillover fs flag:      %s\n"
- "%sSpillover recovery:     "
- "%sStable offset     Head: %llu Tail: %llu\n"
- "%sW2RC:                   %s\n"
- "%sWBC Backoff:            %s\n"
- "%sWBC area:               %llu MiB @ %llu offset, LBA [%llx - %llx]\n"
- "%sWBC checkpoint state:   %u used, %u free\n"
- "%sWBC elevator:           "
- "%sWBC inflightIO lists:   %u initiated; Reads: %u, Writes: %u (WBC: %u, RCWr: %u, bypassed %u)\n"
- "%sWBC list objects:       %llu\n"
- "%sWBC space         Used: %llu MiB (%llu blocks) %.2f%%\n"
- "%sWBC used area LBAs:     [0x%llx - "
- "%sWBC:                    %s\n"
- ", promoting ino# %llu DS# %llu (offset %llu, %llu bytes copied, +%u in queue)\n"
- "0x%llx)\n"
- "0x%llx), [0x%llx - "
- "APFS%sContainer: %s\n"
- "FAILED"
- "Fusion"
- "Main"
- "No"
- "Secondary"
- "TierType"
- "Yes"
- "inactive"
- "off"
- "on"
- "running"
- "running: %llu / %llu\n"
- "sleeping"
- "waiting for data mover"

```
