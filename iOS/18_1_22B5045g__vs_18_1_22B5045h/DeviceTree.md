```diff
 {
   device-tree: {
     children: [
       {
         chosen: {
           children: [
             ...
             ...
             ...
             ...
             ...
             ...
             ...
             ...
             {
               lock-regs: {
-                skip-ioa-regs: 1
               }
             }
             ...
           ]
         }
       }
       {
         port-usb-c-1: {
-          AAPL,phandle: 291
+          AAPL,phandle: 334
         }
       }
       {
         port-inductive-1: {
-          AAPL,phandle: 292
+          AAPL,phandle: 335
         }
       }
       {
         backlight: {
+          EDRAuroraSecondsPerStop: 49152
+          EDRExitSecondsPerStop: 49152
+          grimaldi-sampling-strategy: 1
+          plt-logic-version: 1
-          AAPL,phandle: 293
+          AAPL,phandle: 336
-          EDRSecondsPerStopDefault: 49152
+          EDRSecondsPerStopDefault: 6553
-          LminProduct: 131072
+          LminProduct: 65536
-          backlight-marketing-table: "AAACABNwAwCl+wQAOqMGAGNoCAAmTAoATU8MAGRzDgCwuBAA9h8TAHqpFQDJVhgAXycbAEYcHgB0NCEA6W8kAFnNJwD9SysAT+suAASqMgDQhjYAoH86AJmRPgCoukIANfhGAOpHSwAwp08AGBFUAHKAWADM71wAAFthACC9ZQCAEWoAgFRuAIaDcgDxmnYAppd6AAl3fgBENoIAgsyFAIosiQDQJIwAErWOAJ7skAB22ZIAWYmUAP0IlgCIY5cAZqSYALTVmQAAAJsAHJmmABIhtAAJqcEA/zDPAM+n3gCfHu4Ab5X9AEAMDQHqcR4BbsYxARgsQwGcgFYB/MNrAVoHgQG4SpYB8HytAQKexgEUv98BKOD4ARTwEwLc7jACoO1NAkDbbAK8t40CNJSuAoxf0QK4GfYC6NMaA8xrQwOsA2wDaIqWAwAAwwNwZPEDuLchBOD5UwTgKogEuEq+BEhI+ATQRTIFECFwBQjasQXYgfUFgBg7BuCMhAYQ8M8GADEfB6BPcgcYXccHIDciCAAAfwg="
+          backlight-marketing-table: "AAABAHoUAQCFKwEAj0IBAJlZAQAzcwEAzIwBAGamAQCPwgEAR+EBAHD9AQC4HgIAj0ICADNzAgDCtQIAPQoDAOF6AwDMDAQArscEAI/CBQC4HgcAhesIAIUrCwB61A0AR+EQAK5HFACPAhgArgccAApXIABm5iQAM7MpAFG4LgAU7jMAXE85AJnZPgCPgkQArkdKANcjUADrEVYAPQpcAK4HYgCuB2gAjwJuAKPwcwDr0XkAKJx/AD1KhQCZ2YoAHkWQAI+ClQAAAJsA65GoAPWotgDMTMUAHoXUAApX5AAexfQAmdkFAbieFwHMDCoBUTg9AfUoUQGZ2WUBuF57AeG6kQFR+KgBChfBARQu2gEeRfQBuF4PAh6FKwKux0gCMzNnAlzPhgLXo6cCHsXJAnA97QIKFxID12M4A6MwYAPrkYkDPYq0A1E44QNHoQ8ER+E/BI8CcgQoHKYEcD3cBI+CFAXC9U4FUbiLBbjeygVwfQwGFK5QBj2KlwYULuEGo7AtB1E4fQe43s8HcL0lCAAAfwg="
-          first-paneltype-pab-index: "r"
+          first-paneltype-pab-index: 146
-          gs-b-min: "hAMAAIQDAACEAwAAhAMAAA=="
+          gs-b-min: "hAMAAIQDAACEAwAAhAMAAIQDAACEAwAAhAMAAIQDAACEAwAAhAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEAwAAhAMAAIQDAACEAwAAhAMAAA=="
-          gs-i-nominal: "1AEAAMQBAABAAgAAKwIAAA=="
+          gs-i-nominal: "pgEAAN4BAAD9AQAANQIAAHYBAACaAQAA3QEAAJABAADAAQAA5wEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACZAQAAkwEAAJkBAADdAQAA3QEAAA=="
-          gs-i-threshold: "BgQAAAYEAAAGBAAABgQAAA=="
+          gs-i-threshold: "BgQAAAYEAAAGBAAABgQAAAYEAAAGBAAABgQAAAYEAAAGBAAABgQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBAAABgQAAAYEAAAGBAAABgQAAA=="
-          gs-slope: "9AEAAPQBAAD0AQAA9AEAAA=="
+          gs-slope: "9AEAAPQBAAD0AQAA9AEAAPQBAAD0AQAA9AEAAPQBAAD0AQAA9AEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD0AQAA9AEAAPQBAAD0AQAA9AEAAA=="
-          max-restriction-factors: "8AAIAggCCAKAAugD"
+          max-restriction-factors: "j8J1PrgeBT+4HgU/uB4FPwrXIz8AAIA/"
-          max-restriction-thresholds: "AQAeAFgC6AOIE5Af"
+          max-restriction-thresholds: "AQAAAB4AAABYAgAA6AMAAIgTAACQHwAA"
-          min-restriction-factors: "6APoA7gLuAtwF3AX"
+          min-restriction-factors: "AACAPwAAAEAAAMBAAADAQAAAQEEAAKBC"
-          tw-nits-table: "AAAAQAAAQEAAAIBAAACgQAAAwEAAAOBAAAAAQQAAEEEAACBB"
+          tw-nits-table: "AACAPwAAAEAAAEBAAACAQAAAoEAAAMBAAADgQAAAAEEAABBBAAAgQQ=="
-          tw-strength-table: "AACAPwAAYD8AAEA/AAAgPwAAAD8AAMA+AACAPgAAAD4AAAAAAACAPwAAYD8AAEA/AAAgPwAAAD8AAMA+AACAPgAAAD4AAAAAAACAPwAAYD8AAEA/AAAgPwAAAD8AAMA+AACAPgAAAD4AAAAAAACAPwAAYD8AAEA/AAAgPwAAAD8AAMA+AACAPgAAAD4AAAAAt21bPwAAQD9JkiQ/kiQJP7dt2z5JkqQ+t21bPrdt2z0AAAAASZIkPwAAED9u2/Y+27bNPkmSpD5u23Y+SZIkPkmSpD0AAAAAt23bPgAAwD5JkqQ+kiSJPrdtWz5JkiQ+t23bPbdtWz0AAAAAt21bPgAAQD5JkiQ+kiQJPrdt2z1JkqQ9t21bPbdt2zwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
+          tw-strength-table: "AACAP/OOYz/nHUc/2qwqP807Dj9miOM+TKaqPmaIYz5miOM9AAAAAAAAgD/zjmM/5x1HP9qsKj/NOw4/ZojjPkymqj5miGM+ZojjPQAAAAAAAIA/845jP+cdRz/arCo/zTsOP2aI4z5Mpqo+ZohjPmaI4z0AAAAAAACAP/OOYz/nHUc/2qwqP807Dj9miOM+TKaqPmaIYz5miOM9AAAAAOhqWz/hC0M/2qwqP0VHEj990PM+bxLDPkVHkj5vEkM+MA3DPQAAAAAYlSQ/RUcSPwAAAD92cds+0NW2PkVHkj52cVs+YVQSPuRJkj0AAAAAdnHbPm8Swz5Mpqo+RUeSPn3Qcz5vEkM+YVQSPjANwz0wDUM9AAAAAHZxWz5vEkM+aLMqPmFUEj5GtvM9MA3DPeRJkj0wDUM9MA3DPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
         }
       }
       {
         socd-trace-ram: {
-          AAPL,phandle: 294
+          AAPL,phandle: 338
         }
       }
       {
         baseband: {
-          wlan-idc: 168
+          function-bb_ap_time_sync: [
+            "S"
+            "OIPG"
+          ]
+          function-coredump-h17a: [
+            "OIPGk"
+          ]
+          function-coredump-h17p: [
+            "OIPGl"
+          ]
-          AAPL,phandle: 295
+          AAPL,phandle: 339
-          baseband-heb: 161
+          baseband-heb: 152
-          baseband-idc: 169
+          baseband-idc: 161
           function-bb_on: [
-            "4WKpe0Pg"
-            "s"
+            "8WKpOIcp"
+            "q"
           ]
           function-bb_warm_reset: [
             ...
-            "s"
+            "q"
           ]
-          function-coredump: [
-            "("
-          ]
+          function-coredump: "'"
-          function-pcie_port_control: "CwEAAEN0clAPAQAA"
+          function-pcie_port_control: "LgEAAEN0clAyAQAA"
           function-pmu_exton: [
-            "4RKp60Pg"
-            "s"
+            "8RKpOIcp"
+            "q"
           ]
           function-pmu_exton_config: [
-            "4WKp60Pg"
-            "s"
+            "8WKpOIcp"
+            "q"
           ]
           function-reset_det: [
-            "X"
+            "T"
           ]
           function-sac: [
-            "CCAS0dcl1dcl0mac1mac2mac3mac4mac5mac6mac7mac8mac9macAmacBmacCmacDmacEmacFmacGmacxorp"
+            "CCAS0dcl1dcl0mac1mac2mac3mac4mac5mac6mac7mac8mac9macAmacBmacCmacDmacEmacFmacxorp"
           ]
-          imeisv: 9
+          imeisv: 1
           interrupt-parent: [
-            "X"
-            "s"
+            "T"
+            "q"
           ]
-          interrupts: "GQAAAAQAAAUNAAAA"
+          interrupts: "GwAAAAQAAAUNAAAA"
         }
       }
       {
         amfm: {
+          function-pcie_port_control-pci0: 303
+          function-pcie_port_control-pci2: 308
-          AAPL,phandle: 296
+          AAPL,phandle: 340
-          function-pcie_port_control: "CwEAAEN0clAMAQAA"
+          function-pcie_port_control: [
+            "CtrP"
+          ]
           function-reg_on: [
-            "4WKp80Pg"
-            "s"
+            "8WKpOIcp"
+            "q"
           ]
         }
       }
       {
         sacm-general: {
-          AAPL,phandle: 297
+          AAPL,phandle: 341
         }
       }
       {
         sacm-jasper: {
-          AAPL,phandle: 298
+          AAPL,phandle: 342
         }
       }
       {
         defaults: {
+          pmap-io-ranges-h17a: "AAACjQIAAAAAwAAAAAAAAAdAAABUUkFE"
+          pmap-io-ranges-h17p: "AAACjQIAAAAAwAAAAAAAAAdAAABUUkFEAAAIjQIAAAAAwAAAAAAAAAdAAABUUkFE"
-          AAPL,phandle: 299
+          AAPL,phandle: 343
           pmap-io-ranges: [
             {
-              start: 24159191040
+              start: 49392123904
-              size: 1610612736
+              size: 1073741824
             }
             {
-              start: 12082757632
+              start: 17363959808
             }
-            {
-              start: 30114054144
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 30114578432
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 30114316288
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
-            {
-              start: 30114840576
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
-            {
-              start: 13270810624
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13237420032
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13237485568
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13237501952
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
-            {
-              start: 13237354496
-              size: 16384
-              flags: 16391
-              name: "SMMU"
-            }
-            {
-              start: 11287658496
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
             {
-              start: 10888478720
+              start: 11089870848
-              size: 16384
+              size: 131072
             }
-            {
-              start: 13178503168
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13178519552
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
-            {
-              start: 13178568704
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13178634240
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 11223973888
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 11224023040
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13373538304
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 11178524672
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
             {
-              start: 11178541056
+              start: 13046054912
             }
             {
-              start: 11358191616
+              start: 13019774976
-              size: 16384
+              size: 131072
             }
             {
-              start: 11178557440
+              start: 15264399360
-              name: "SMMU"
+              name: "SRT4"
             }
             {
-              start: 11178573824
+              start: 13045989376
-              size: 16384
+              size: 49152
             }
-            {
-              start: 11178590208
-              size: 16384
-              flags: 16391
-              name: "SMMU"
-            }
             {
-              start: 11178606592
+              start: 15116599296
-              name: "DART"
+              name: "HMAC"
             }
             {
-              flags: 16391
-              start: 10958684160
+              start: 11811160064
-              size: 16384
+              size: 402653184
-              name: "DART"
+              name: "SKIO"
             }
             {
-              flags: 16391
-              start: 10958667776
+              start: 13958643712
-              size: 16384
+              size: 603881472
-              name: "SMMU"
+              name: "SKIO"
             }
             {
-              flags: 16391
-              start: 10958716928
+              start: 16106127360
-              size: 16384
+              size: 231473152
-              name: "DART"
+              name: "SKIO"
             }
             {
-              flags: 16391
-              start: 10958995456
+              start: 16337666048
-              size: 16384
+              size: 3145728
-              name: "DART"
+              name: "SKIO"
             }
             {
-              flags: 16391
-              start: 10958979072
+              start: 16374562816
-              size: 16384
+              size: 402653184
-              name: "SMMU"
+              name: "SKIO"
             }
             {
-              flags: 16391
-              start: 10958733312
+              start: 18253611008
-              size: 16384
+              size: 402653184
-              name: "DAPF"
+              name: "SKIO"
             }
-            {
-              start: 11358208000
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
             {
-              start: 10958815232
+              start: 17485463552
             }
             {
-              flags: 16391
-              start: 10958831616
+              start: 10787749888
-              size: 16384
+              size: 32768
-              name: "GAPF"
+              name: "SKIO"
             }
-            {
-              start: 10958848000
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 10958864384
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 10958880768
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 10958897152
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 13307494400
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13307527168
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 13307478016
-              size: 16384
-              flags: 16391
-              name: "SMMU"
-            }
-            {
-              start: 13307543552
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
             {
-              start: 12692062208
+              start: 15384838144
-              size: 16384
+              size: 131072
             }
-            {
-              start: 13307625472
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 13307641856
-              size: 16384
-              flags: 16391
-              name: "GAPF"
-            }
-            {
-              start: 24126160896
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 24126177280
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
             {
-              start: 23957864448
+              start: 15300820992
-              size: 16384
+              size: 131072
             }
-            {
-              start: 23974641664
-              size: 16384
-              flags: 16391
-              name: "DSID"
-            }
-            {
-              start: 23991418880
-              size: 16384
-              flags: 16391
-              name: "DSID"
-            }
             {
-              start: 13116538880
+              start: 15264022528
             }
-            {
-              start: 13116604416
-              size: 16384
-              flags: 16391
-              name: "NVMe"
-            }
-            {
-              start: 13104054272
-              size: 278528
-              flags: 16391
-              name: "NVMe"
-            }
             {
-              start: 12692078592
+              start: 13169917952
             }
             {
-              start: 13115916288
+              start: 15263399936
             }
-            {
-              start: 12418531328
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
-            {
-              start: 12418514944
-              size: 16384
-              flags: 16391
-              name: "DAPF"
-            }
-            {
-              start: 12415762432
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
             {
-              size: 16384
+              size: 32768
             }
             ...
             {
-              size: 16384
+              size: 32768
             }
             ...
             {
-              size: 16384
+              size: 32768
             }
             ...
-            {
-              start: 12792659968
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
             {
-              size: 16384
+              size: 32768
             }
             ...
-            {
-              start: 11039408128
-              size: 327680
-              flags: 16391
-              name: "DENY"
-            }
-            {
-              start: 11040522240
-              size: 3080192
-              flags: 16391
-              name: "DENY"
-            }
-            {
-              start: 8858697728
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
-            {
-              start: 8859746304
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
-            {
-              start: 8860794880
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
-            {
-              start: 8861843456
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
-            {
-              start: 8875474944
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
-            {
-              start: 8876523520
-              size: 16384
-              flags: 16391
-              name: "RVBR"
-            }
             {
-              start: 12792676352
+              start: 17552441344
             }
-            {
-              start: 12082741248
-              size: 16384
-              flags: 16391
-              name: "DART"
-            }
+            {
+              start: 50465865728
+              size: 536870912
+              flags: 39
+              name: "PCIe"
+            }
+            {
+              start: 123211874304
+              size: 81920
+              flags: 2147483655
+              name: "PCIe"
+            }
+            {
+              start: 17485332480
+              size: 16384
+              flags: 16391
+              name: "DAPF"
+            }
+            {
+              start: 17363435520
+              size: 16384
+              flags: 16391
+              name: "DAPF"
+            }
+            {
+              start: 17485479936
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17485496320
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17485512704
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17485529088
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17485545472
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17552572416
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 17552588800
+              size: 16384
+              flags: 16391
+              name: "GAPF"
+            }
+            {
+              start: 15317598208
+              size: 131072
+              flags: 16391
+              name: "DSID"
+            }
+            {
+              start: 15334375424
+              size: 131072
+              flags: 16391
+              name: "DSID"
+            }
+            {
+              start: 15264088064
+              size: 16384
+              flags: 16391
+              name: "NVMe"
+            }
+            {
+              start: 16337600512
+              size: 65536
+              flags: 16391
+              name: "NVMe"
+            }
+            {
+              start: 15263072256
+              size: 16384
+              flags: 16391
+              name: "NVMe"
+            }
+            {
+              start: 15263203328
+              size: 16384
+              flags: 16391
+              name: "NVMe"
+            }
+            {
+              start: 15262023680
+              size: 131072
+              flags: 16391
+              name: "NVMe"
+            }
+            {
+              start: 20401094656
+              size: 67108864
+              name: "SKIO"
+            }
           ]
-          serial-device: "~"
+          serial-device: "}"
         }
       }
       {
         product: {
+          camera-button-location: "bigKAKwVFgC/oQ0AJvYBABAnAAA="
+          supports-camera-button: 1
+          supports-recoveryos: 1
-          AAPL,phandle: 300
+          AAPL,phandle: 344
-          artwork-device-subtype: 2796
+          artwork-device-subtype: 2622
-          baseband-chipset: "mav23"
+          baseband-chipset: "mav24"
-          bmu-board-id: "4("
+          bmu-board-id: "#("
           children: [
             {
               camera: {
-                AAPL,phandle: 301
+                AAPL,phandle: 345
-                aggregate-cam-photo-zoom: 2500
+                aggregate-cam-photo-zoom: 2000
-                aggregate-cam-video-zoom: 1500
+                aggregate-cam-video-zoom: 1200
-                rear-max-video-fps-1080p: "<"
+                rear-max-video-fps-1080p: "x"
-                rear-max-video-fps-4k: "<"
+                rear-max-video-fps-4k: "x"
               }
             }
             {
               facetime: {
-                AAPL,phandle: 302
+                AAPL,phandle: 346
               }
             }
             {
               maps: {
-                AAPL,phandle: 303
+                AAPL,phandle: 347
               }
             }
             {
               haptics: {
-                AAPL,phandle: 304
+                AAPL,phandle: 348
               }
             }
             {
               audio: {
-                mic-trim-gains-1: "syscfg/MiGB"
+                mic-trim-gains-2: "syscfg/MiGB"
-                AAPL,phandle: 305
+                AAPL,phandle: 349
-                acoustic-id: 8011
+                acoustic-id: 8016
-                actuator-cpms-bgd_100ms: 16488379449844
+                actuator-cpms-bgd_100ms: 16419659973108
-                actuator-cpms-bgd_inst: 32641751451376
+                actuator-cpms-bgd_inst: 32641751451350
-                historyChannels: 1
+                historyChannels: 15
-                speaker-cpms-bgd_100ms: 31181462570741
+                speaker-cpms-bgd_100ms: [
+                  "(#"
+                ]
-                speaker-cpms-bgd_1s: 31181462569831
+                speaker-cpms-bgd_1s: [
+                  "(#"
+                ]
                 speaker-cpms-bgd_inst: [
-                  "Bc"
+                  "(#"
                 ]
               }
             }
           ]
-          chrome-identifier: "com.apple.dt.devicekit.chrome.phone8"
+          chrome-identifier: "com.apple.dt.devicekit.chrome.phone11"
-          compatible-device-fallback: "iPhone15,3"
+          compatible-device-fallback: "iPhone16,1"
           display-corner-radius: [
-            "7"
+            ">"
           ]
-          exclaves-enabled: 0
+          exclaves-enabled: 1
-          framebuffer-identifier: "35673A77-95F0-41BF-A6EE-BA5C7D4C8C98"
+          framebuffer-identifier: "4E5532ED-1470-47D1-BDF4-7AA90C26957A"
-          front-cam-offset-from-center: "QRoBAK0cAAA9FAAA6AMAAAAAAAA="
+          front-cam-offset-from-center: "xQUBAK0cAAA+FAAA6AMAAAAAAAA="
-          has-exclaves: 0
+          has-exclaves: 1
-          large-format-phone: 1
+          large-format-phone: 0
-          product-description: "iPhone 15 Pro Max"
+          product-description: "iPhone 16 Pro"
-          product-id: "pnq4GS0xTmfvGyH3mqsNnkXubdE="
+          product-id: "o1H/oWeYZVdLwNSeZ01WPjuZaUg="
-          product-name: "iPhone 15 Pro Max"
+          product-name: "iPhone 16 Pro"
-          rear-cam-offset-from-center: "vLUAAIdeAACoCQAA6AMAAAAAAAA="
+          rear-cam-offset-from-center: [
+            "6T"
+          ]
-          ringer-button-location: "lLYKAOiMFwAE8wMAQOwAABAnAAA="
+          ringer-button-location: "bigKAKwVFgBKTQQAiA0BABAnAAA="
-          side-button-location: "lLYKAOiMFwAk0AYAQLMCABAnAAA="
+          side-button-location: "bigKAKwVFgCHuAYANrMCABAnAAA="
-          volume-down-button-location: "lLYKAOiMFwBqygcAgLUBABAnAAA="
+          volume-down-button-location: "bigKAKwVFgC6TAgAgLUBABAnAAA="
-          volume-up-button-location: "lLYKAOiMFwC6nwUAgLUBABAnAAA="
+          volume-up-button-location: "bigKAKwVFgAUIgYAgLUBABAnAAA="
-          wifi-chipset: "4388"
+          wifi-chipset: "4399"
         }
       }
       ...
       {
         filesystems: {
-          AAPL,phandle: 306
+          AAPL,phandle: 350
           children: [
             {
               fstab: {
-                AAPL,phandle: 307
+                AAPL,phandle: 351
                 children: [
                   {
                     xart-vol: {
-                      AAPL,phandle: 308
+                      AAPL,phandle: 352
                     }
                   }
                   {
                     system-vol: {
-                      AAPL,phandle: 309
+                      AAPL,phandle: 353
                     }
                   }
                   {
                     preboot-vol: {
-                      AAPL,phandle: 310
+                      AAPL,phandle: 354
                     }
                   }
                   {
                     data-vol: {
-                      AAPL,phandle: 311
+                      AAPL,phandle: 355
                     }
                   }
                   {
                     baseband-vol: {
-                      AAPL,phandle: 312
+                      AAPL,phandle: 356
                     }
                   }
                   {
                     update-vol: {
-                      AAPL,phandle: 313
+                      AAPL,phandle: 357
                     }
                   }
                   {
                     hardware-vol: {
-                      AAPL,phandle: 314
+                      AAPL,phandle: 358
                     }
                   }
                 ]
               }
             }
             {
               fstab-ephemeral-recovery-data: {
-                AAPL,phandle: 315
+                AAPL,phandle: 359
                 children: [
                   {
                     ephemeral-recovery-data-vol: {
-                      AAPL,phandle: 316
+                      AAPL,phandle: 360
                     }
                   }
                   {
                     preboot-vol: {
-                      AAPL,phandle: 317
+                      AAPL,phandle: 361
                     }
                   }
                   {
                     hardware-vol: {
-                      AAPL,phandle: 318
+                      AAPL,phandle: 362
                     }
                   }
                 ]
               }
             }
             {
               fstab-ephemeral-diag-data: {
-                AAPL,phandle: 319
+                AAPL,phandle: 363
                 children: [
                   {
                     ephemeral-diag-data-vol: {
-                      AAPL,phandle: 320
+                      AAPL,phandle: 364
                     }
                   }
                   {
                     baseband-vol: {
-                      AAPL,phandle: 321
+                      AAPL,phandle: 365
                     }
                   }
                   {
                     update-vol: {
-                      AAPL,phandle: 322
+                      AAPL,phandle: 366
                     }
                   }
                   {
                     preboot-vol: {
-                      AAPL,phandle: 323
+                      AAPL,phandle: 367
                     }
                   }
                   {
                     hardware-vol: {
-                      AAPL,phandle: 324
+                      AAPL,phandle: 368
                     }
                   }
                 ]
               }
             }
           ]
         }
       }
       {
         fillmore: {
-          AAPL,phandle: 325
+          AAPL,phandle: 369
         }
       }
       {
         iboot-syscfg: {
-          AAPL,phandle: 326
+          AAPL,phandle: 370
           children: [
             {
               manifest-entitlements: {
-                AAPL,phandle: 327
+                AAPL,phandle: 371
               }
             }
           ]
         }
       }
       {
         osenvironments: {
-          AAPL,phandle: 328
+          AAPL,phandle: 372
           children: [
             {
               recovery-environment: {
-                AAPL,phandle: 329
+                AAPL,phandle: 373
                 children: [
                   {
                     ephemeral-recovery-data-volume: {
-                      AAPL,phandle: 330
+                      AAPL,phandle: 374
                     }
                   }
                   {
                     ephemeral-storage: {
-                      AAPL,phandle: 331
+                      AAPL,phandle: 375
                     }
                   }
                   {
                     no-sepfw-load-at-boot: {
-                      AAPL,phandle: 332
+                      AAPL,phandle: 376
                     }
                   }
                   {
                     no-protected-data-access: {
-                      AAPL,phandle: 333
+                      AAPL,phandle: 377
                     }
                   }
                   {
                     amfi-allows-trust-cache-load: {
-                      AAPL,phandle: 334
+                      AAPL,phandle: 378
                     }
                   }
                   {
                     disable-av-content-protection: {
-                      AAPL,phandle: 335
+                      AAPL,phandle: 379
                     }
                   }
                   {
                     use-recovery-securityd: {
-                      AAPL,phandle: 336
+                      AAPL,phandle: 380
                     }
                   }
                   {
                     disable-accessory-firmware: {
-                      AAPL,phandle: 337
+                      AAPL,phandle: 381
                     }
                   }
                   {
                     image4-allow-magazine-updates: {
-                      AAPL,phandle: 338
+                      AAPL,phandle: 382
                     }
                   }
                 ]
               }
             }
             {
               diagnostics-environment: {
-                AAPL,phandle: 339
+                AAPL,phandle: 383
                 children: [
                   {
                     ephemeral-diag-data-volume: {
-                      AAPL,phandle: 340
+                      AAPL,phandle: 384
                     }
                   }
                   {
                     ephemeral-storage: {
-                      AAPL,phandle: 341
+                      AAPL,phandle: 385
                     }
                   }
                   {
                     disable-transport-rm: {
-                      AAPL,phandle: 342
+                      AAPL,phandle: 386
                     }
                   }
                   {
                     no-protected-data-access: {
-                      AAPL,phandle: 343
+                      AAPL,phandle: 387
                     }
                   }
                   {
                     amfi-allows-trust-cache-load: {
-                      AAPL,phandle: 344
+                      AAPL,phandle: 388
                     }
                   }
                 ]
               }
             }
             {
               darwinos-ramdisk-environment: {
-                AAPL,phandle: 345
+                AAPL,phandle: 389
                 children: [
                   {
                     isp-horizon: {
-                      AAPL,phandle: 346
+                      AAPL,phandle: 390
                     }
                   }
                   {
                     ephemeral-recovery-data-volume: {
-                      AAPL,phandle: 347
+                      AAPL,phandle: 391
                     }
                   }
                   {
                     ephemeral-storage: {
-                      AAPL,phandle: 348
+                      AAPL,phandle: 392
                     }
                   }
                   {
                     no-protected-data-access: {
-                      AAPL,phandle: 349
+                      AAPL,phandle: 393
                     }
                   }
                   {
                     no-sepfw-load-at-boot: {
-                      AAPL,phandle: 350
+                      AAPL,phandle: 394
                     }
                   }
                 ]
               }
             }
             {
               macos-darwinos-environment: {
-                AAPL,phandle: 351
+                AAPL,phandle: 395
                 children: [
                   {
                     set-macos-darwinos-env: {
-                      AAPL,phandle: 352
+                      AAPL,phandle: 396
                     }
                   }
                 ]
               }
             }
             {
               embedded-darwinos-environment: {
-                AAPL,phandle: 353
+                AAPL,phandle: 397
                 children: [
                   {
                     set-embedded-darwinos-env: {
-                      AAPL,phandle: 354
+                      AAPL,phandle: 398
                     }
                   }
                 ]
               }
             }
             {
               trusted-darwinos-environment: {
-                AAPL,phandle: 355
+                AAPL,phandle: 399
                 children: [
                   {
                     set-trusted-darwinos-env: {
-                      AAPL,phandle: 356
+                      AAPL,phandle: 400
                     }
                   }
                 ]
               }
             }
             {
               repair-environment: {
-                AAPL,phandle: 357
+                AAPL,phandle: 401
                 children: [
                   {
                     set-repair-env: {
-                      AAPL,phandle: 358
+                      AAPL,phandle: 402
                     }
                   }
                 ]
               }
             }
           ]
         }
       }
+      {
+        exbright: {
+          AAPL,phandle: 337
+          als-types: 9
+          alss-available: 1
+          alss-calibration: "syscfg/AlsS"
+          alss-gain: 512
+          alss-subsamples: 335
+          children: [
+          ]
+          exclave-assigned: null
+          exclave-edk-endpoint: 22
+          exclave-endpoint: 21
+          fdr-class: 1
+          panel-typical-freq: "x"
+          product: 1
+        }
+      }
+      {
+        exclaves-test: {
+          AAPL,phandle: 403
+          children: [
+          ]
+          compatible: [
+            "exclaves-test"
+            "sgx"
+          ]
+          exclave-assigned: null
+          exclave-edk-endpoint: 9
+          exclave-endpoint: 3
+        }
+      }
       {
         cpus: {
           children: [
             {
               cpu0: {
-                cpm-impl-reg: "AADkEAIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEAIAAAAQwAAAAAAAAA=="
               }
             }
             {
               cpu1: {
-                cpm-impl-reg: "AADkEAIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEAIAAAAQwAAAAAAAAA=="
               }
             }
             {
               cpu2: {
-                cpm-impl-reg: "AADkEAIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEAIAAAAQwAAAAAAAAA=="
               }
             }
             {
               cpu3: {
-                cpm-impl-reg: "AADkEAIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEAIAAAAQwAAAAAAAAA=="
               }
             }
             {
               cpu4: {
-                l2-cache-size: 16777216
+                l2-cache-size-h17a: 8388608
+                l2-cache-size-h17p: 16777216
-                cpm-impl-reg: "AADkEQIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEQIAAAAQwAAAAAAAAA=="
-                interrupts: "x"
+                interrupts: "l"
               }
             }
             {
               cpu5: {
-                l2-cache-size: 16777216
+                l2-cache-size-h17a: 8388608
+                l2-cache-size-h17p: 16777216
-                cpm-impl-reg: "AADkEQIAAAAosAAAAAAAAA=="
+                cpm-impl-reg: "AADkEQIAAAAQwAAAAAAAAA=="
-                interrupts: "{"
+                interrupts: "o"
               }
             }
           ]
         }
       }
       ...
       ...
       ...
       ...
       {
         arm-io: {
           children: [
             {
               aic: {
                 reg: {
-                  addr: 3238002688
+                  addr: 4043309056
                 }
               }
             }
             {
               pwm: {
-                AAPL,phandle: 44
+                AAPL,phandle: 43
-                clock-gates: "8"
+                clock-gates: "@"
-                interrupts: 889
+                interrupts: 1117
                 reg: {
-                  addr: 2500067328
+                  addr: 6258163712
                 }
               }
             }
             {
-              alc4: {
-                AAPL,phandle: 265
-                alc-number: 4
-                children: [
-                  {
-                    audio-leap-mca-loopback: {
-                      AAPL,phandle: 266
-                      audio-stream-formatter: "pael"
-                      children: [
-                      ]
-                      compatible: "audio-data,external"
-                      data-sources: [
-                        "Leap loopback"
-                      ]
-                      device-name: "LEAP MCA Loopback"
-                      device-uid: "LEAP MCA Loopback"
-                      device_type: "leap-audio-data"
-                      reg: "AEIAAAIAAQAAG7cA+gABADAAAQABAAAAAwAAAAECICADAAAA"
-                    }
-                  }
-                ]
-                clock-domain: "niam"
-                compatible: "alc,t8130"
-                device_type: "i2s"
-                dma-channels: [
-                  "!"
-                  "`"
-                  "!"
-                  "\""
-                  "`"
-                  "\""
-                ]
-                dma-parent: 237
-                external-power-provider: [
-                  "F"
-                ]
-                function-admac_powerswitch: [
-                  "CSPa"
-                ]
-                function-aop-device-control: [
-                  "F"
-                  "ltCg"
-                ]
-                function-aop-device-control-id: "blpl"
-              }
+              admac-leap-ns: {
+                #dma-channels: 9
+                AAPL,phandle: 297
+                channel-buffer-alloc-base-rx: 0
+                channel-buffer-alloc-base-tx: 0
+                channel-buffer-allocation: "AA4AAAAAAAAAEQAAAAAAAA=="
+                channels-offset: 0
+                children: [
+                ]
+                clock-gates: 299
+                compatible: "admac,t8140"
+                device_type: "admac"
+                interrupt-parent: " "
+                interrupts: 452
+                iommu-parent: "L"
+                irq-destination-index: 0
+                irq-destinations: " CIAUPCA NTGDSNU"
+                reg: [
+                  {
+                    addr: 4348444672
+                    size: 212992
+                  }
+                  {
+                    addr: 4163534848
+                    size: 8
+                  }
+                ]
+                role: "SNEL"
+                service-exclave_proxy: null
+              }
             }
             {
               apcie: {
-                AAPL,phandle: 267
+                AAPL,phandle: 302
                 children: [
                   {
                     pci-bridge0: {
+                      function-perst-tahiti: "OIPGr"
+                      function-perst-tupai: "OIPGp"
-                      AAPL,phandle: 268
+                      AAPL,phandle: 303
                       children: [
                         {
                           wlan: {
-                            iommu-parent: 274
+                            iommu-parent-pcie0: 312
+                            iommu-parent-pcie2: 317
-                            AAPL,phandle: 269
+                            AAPL,phandle: 304
                           }
                         }
                         {
                           bluetooth-pcie: {
-                            iommu-parent: 275
+                            iommu-parent-pcie0: 313
+                            iommu-parent-pcie2: 318
-                            AAPL,phandle: 270
+                            AAPL,phandle: 305
                           }
                         }
                       ]
-                      default-apcie-options: 2147483648
+                      default-apcie-options: 2214592512
                       function-clkreq: [
-                        "("
+                        "'"
+                        "OIPGe"
                       ]
-                      function-perst: [
-                        "("
-                      ]
+                      function-perst: "'"
-                      maximum-link-speed: 2
+                      maximum-link-speed: 3
                     }
                   }
                   {
                     pci-bridge1: {
+                      function-clkreq-tahiti: [
+                        "OIPGp"
+                      ]
+                      function-clkreq-tupai: [
+                        "OIPGo"
+                      ]
+                      function-perst-tahiti: "OIPGs"
+                      function-perst-tupai: "OIPGq"
-                      AAPL,phandle: 271
+                      AAPL,phandle: 306
                       children: [
                         {
                           baseband-pcie: {
-                            AAPL,phandle: 272
+                            AAPL,phandle: 307
-                            iommu-parent: 277
+                            iommu-parent: 315
                           }
                         }
                       ]
-                      function-clkreq: [
-                        "("
-                      ]
+                      function-clkreq: "'"
-                      function-perst: [
-                        "("
-                      ]
+                      function-perst: "'"
                     }
                   }
+                  {
+                    pci-bridge2: {
+                      #address-cells: 1
+                      #msi-vectors: " "
+                      #size-cells: 0
+                      AAPL,phandle: 308
+                      AAPL,unit-string: "00020000"
+                      apcie-port: 2
+                      built-in: null
+                      children: [
+                        {
+                          wlan: {
+                            #address-cells: 1
+                            #size-cells: 0
+                            AAPL,phandle: 309
+                            AAPL,unit-string: "00000000"
+                            built-in: null
+                            cfg-io-timeout: "AAAAAAAQAABQwwAA"
+                            children: [
+                            ]
+                            compatible: [
+                              "wlan-pcie,bcm4387"
+                              "wlan-pcie,bcm"
+                            ]
+                            crash-terminate-self-only: null
+                            device_type: "pcie-device"
+                            iommu-parent-pcie0: 312
+                            iommu-parent-pcie2: 317
+                            mem-io-timeout: "6CEAAAQAAABQwwAA"
+                            pci-aspm-default: 2
+                            pci-l1pm-control: [
+                              "U@H"
+                            ]
+                            pci-max-latency: 268963848
+                          }
+                        }
+                        {
+                          bluetooth-pcie: {
+                            #address-cells: 1
+                            #size-cells: 0
+                            AAPL,phandle: 310
+                            AAPL,unit-string: "00000001"
+                            cfg-io-timeout: "AAAAAAAQAABQwwAA"
+                            children: [
+                            ]
+                            compatible: [
+                              "wlan-pcie,bcm4387"
+                              "wlan-pcie,bcm"
+                            ]
+                            device_type: "pcie-device"
+                            iommu-parent-pcie0: 313
+                            iommu-parent-pcie2: 318
+                            mem-io-timeout: "6CEAAAQAAABQwwAA"
+                            pci-aspm-default: 2
+                            pci-max-latency: 268963848
+                          }
+                        }
+                      ]
+                      compatible: "apcie-bridge"
+                      default-apcie-options: 2214592512
+                      enable-ptm: null
+                      function-clkreq: [
+                        "'"
+                        "OIPGq"
+                      ]
+                      function-dart_force_active: [
+                        "tcaF"
+                      ]
+                      function-dart_release_sid: [
+                        "leRS"
+                      ]
+                      function-dart_request_sid: [
+                        "qeRS"
+                      ]
+                      function-dart_self: [
+                        "fleS"
+                      ]
+                      function-perst: [
+                        "'"
+                      ]
+                      lpem-workaround: null
+                      manual-enable: null
+                      manual-enable-s2r: null
+                      maximum-link-speed: 3
+                      msi-vector-base: "@"
+                      pci-l1pm-control: 172878005263
+                      perst-to-config: "d"
+                      t-refclk-to-perst: "d"
+                    }
+                  }
                 ]
                 clock-gates: [
-                  "2"
-                  "6"
-                  "D"
-                  "U"
+                  "5"
+                  "9"
+                  ">"
+                  "L"
+                  "^"
+                  "b"
                 ]
-                compatible: "apcie,t8130"
+                compatible: "apcie,t8140"
                 function-debug_gpio: [
-                  "("
-                  "OIPGI"
+                  "'"
+                  "OIPG5"
                 ]
-                interrupts: "1wMAAOADAADpAwAA"
+                interrupts: "tQQAAL4EAADHBAAA"
-                msi-vector-offset: 1102
+                msi-vector-offset: 1331
                 power-gates: [
-                  "2"
-                  "6"
-                  "D"
-                  "U"
+                  "5"
+                  "9"
+                  ">"
+                  "L"
+                  "^"
+                  "b"
                 ]
-                ranges: "AAAAQwAAAKAFAAAAAAAAoAUAAAAAAAAgAAAAAAAAAAIAAADAAAAAAAAAAMAFAAAAAAAAQAAAAAA="
+                ranges: "AAAAQwAAAMALAAAAAAAAwAsAAAAAAAAgAAAAAAAAAAIAAACAAAAAAAAAAIALAAAAAAAAQAAAAAA="
                 reg: [
                   {
-                    addr: 23622320128
+                    addr: 123211874304
                   }
                   {
-                    addr: 24125685760
+                    addr: 15418392576
                   }
                   {
-                    addr: 24125931520
+                    addr: 15317762048
                   }
                   {
-                    addr: 23957880832
+                    addr: 15317843968
                   }
-                  {
-                    addr: 23974674432
-                    size: 32768
-                  }
                   {
-                    addr: 23974756352
+                    addr: 15418408960
                   }
                   {
-                    addr: 24125702144
+                    addr: 15317745664
                   }
                   {
-                    addr: 24125964288
+                    addr: 15334539264
                   }
                   {
-                    addr: 23974658048
+                    addr: 15334621184
                   }
-                  {
-                    addr: 23991451648
-                    size: 32768
-                  }
                   {
-                    addr: 23991533568
+                    addr: 15334522880
                   }
                   {
-                    addr: 23907532800
+                    addr: 15367929856
                   }
-                  {
-                    addr: 24125718528
-                    size: 16384
-                  }
-                  {
-                    addr: 24125997056
-                    size: 32768
-                  }
-                  {
-                    addr: 23991435264
-                    size: 16384
-                  }
-                  {
-                    addr: 24125636608
-                    size: 49152
-                  }
+                  {
+                    addr: 15418523648
+                    size: 163840
+                  }
+                  {
+                    addr: 15300968448
+                    size: 16384
+                  }
+                  {
+                    addr: 15418425344
+                    size: 16384
+                  }
                   {
-                    addr: 24125898752
+                    addr: 15418261504
                   }
                   {
-                    addr: 24092082176
+                    addr: 15401484288
-                    size: 32768
+                    size: 16777216
                   }
                   {
-                    addr: 24126202368
+                    addr: 15384994304
                   }
                   {
-                    addr: 24126193664
+                    addr: 15384985600
                   }
                   {
-                    addr: 23957897216
+                    addr: 15300984832
                   }
                   {
-                    addr: 23957979136
+                    addr: 15301066752
                   }
                 ]
               }
             }
             {
               dart-apcie0: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
-                AAPL,phandle: 273
+                AAPL,phandle: 311
                 children: [
                   {
                     mapper-apcie0-wlan: {
-                      AAPL,phandle: 274
+                      AAPL,phandle: 312
                     }
                   }
                   {
                     mapper-apcie0-bt: {
-                      AAPL,phandle: 275
+                      AAPL,phandle: 313
                     }
                   }
                 ]
-                interrupts: 984
+                interrupts: 1206
                 reg: {
-                  addr: 23957864448
+                  addr: 15300820992
-                  size: 16384
+                  size: 131072
                 }
               }
             }
             {
               dart-apcie1: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
-                AAPL,phandle: 276
+                AAPL,phandle: 314
                 children: [
                   {
                     mapper-apcie1: {
-                      AAPL,phandle: 277
+                      AAPL,phandle: 315
                     }
                   }
                 ]
-                interrupts: 993
+                interrupts: 1215
                 reg: {
-                  addr: 23974641664
+                  addr: 15317598208
-                  size: 16384
+                  size: 131072
                 }
               }
             }
             {
               smctempsensor0: {
-                AAPL,phandle: 278
+                AAPL,phandle: 319
               }
             }
             {
               cpu-debug-interface: {
-                cpu_halt: null
-                enable_alt_trace: "AADpAAAAAAAoAQAAAAAAAGAADwAAAAAAAAAAgAAAAADYAA8AAAAAAAAAAAICAAAA/////wAAAAAAAAAAAAAAAAAA6QEAAAAAKAEAAAAAAABgADAAAAAAAAAAAIAAAAAA2AAwAAAAAAAAAAACAgAAAP////8AAAAAAAAAAAAAAAAAAAUAAAAAABCQAAAAAAAACAABAAAAAAAFAAAAAAAAAAgAAQAAAAAACwAQAgAAAAD/////AAAAAAAAAAAAAAAAAAAVAAAAAAAQkAAAAAAAAAgAAgAAAAAABQAAAAAAAAAIAAIAAAAAAAsAEAIAAAAA/////wAAAAAAAAAAAAAAAAAAJQAAAAAAEJAAAAAAAAAIAAQAAAAAAAUAAAAAAAAACAAEAAAAAAALABACAAAAAP////8AAAAAAAAAAAAAAAAAADUAAAAAABCQAAAAAAAACAAIAAAAAAAFAAAAAAAAAAgACAAAAAAACwAQAgAAAAD/////AAAAAAAAAAAAAAAAAAAFAQAAAAAQkAAAAAAAAAgAEAAAAAAABQAAAAAAAAAIABAAAAAAAAsAEAIAAAAA/////wAAAAAAAAAAAAAAAAAAFQEAAAAAEJAAAAAAAAAIACAAAAAAAAUAAAAAAAAACAAgAAAAAAALABACAAAAAP////8AAAAAAAAAAAAAAAAAAOUAAAAAAECQAAAAAAAA8AAPAAAAAAAKDwAAAAAAAP////8AAAAAAAAAAAAAAAAAAOkAAAAAACgBAAAAAAAA2AAPAAAAAAAAAACFAgAAAP////8AAAAAAAAAAAAAAAAAAOUBAAAAAECQAAAAAAAA8AAwAAAAAAAKDwAAAAAAAP////8AAAAAAAAAAAAAAAAAAOkBAAAAACgBAAAAAAAA2AAwAAAAAAAAAACFAgAAAA=="
-                enable_trace: "AADpAAAAAAAoAQAAAAAAAGAADwAAAAAAAAAAgAAAAADYAA8AAAAAAAAAAAICAAAA/////wAAAAAAAAAAAAAAAAAA6QEAAAAAKAEAAAAAAABgADAAAAAAAAAAAIAAAAAA2AAwAAAAAAAAAAACAgAAAP////8AAAAAAAAAAAAAAAAAAAUAAAAAABCQAAAAAAAACAABAAAAAAAFAAAAAAAAAAgAAQAAAAAACwAQAgAAAAD/////AAAAAAAAAAAAAAAAAAAVAAAAAAAQkAAAAAAAAAgAAgAAAAAABQAAAAAAAAAIAAIAAAAAAAsAEAIAAAAA/////wAAAAAAAAAAAAAAAAAAJQAAAAAAEJAAAAAAAAAIAAQAAAAAAAUAAAAAAAAACAAEAAAAAAALABACAAAAAP////8AAAAAAAAAAAAAAAAAADUAAAAAABCQAAAAAAAACAAIAAAAAAAFAAAAAAAAAAgACAAAAAAACwAQAgAAAAD/////AAAAAAAAAAAAAAAAAAAFAQAAAAAQkAAAAAAAAAgAEAAAAAAABQAAAAAAAAAIABAAAAAAAAsAEAIAAAAA/////wAAAAAAAAAAAAAAAAAAFQEAAAAAEJAAAAAAAAAIACAAAAAAAAUAAAAAAAAACAAgAAAAAAALABACAAAAAP////8AAAAAAAAAAAAAAAAAAOkAAAAAACgBAAAAAAAA2AAPAAAAAAAAAACFAgAAAP////8AAAAAAAAAAAAAAAAAAOkBAAAAACgBAAAAAAAA2AAwAAAAAAAAAACFAgAAAA=="
-                trace_halt: "AADlAAAAAABAkAAAAAAAALAADwAAAAAAAAAAAA8AAAD/////AAAAAAAAAAAAAAAAAADlAQAAAABAkAAAAAAAALAAMAAAAAAAAAAAAA8AAAA="
+                panic-trace-mode: 4
-                AAPL,phandle: 279
+                AAPL,phandle: 320
-                aft-control-list: 9127919616
+                aft-control-list: 10032840704
-                aft-instance-list: "AAARIAIAAABBRlQAAAAAAAAAAAAAAAAA"
+                aft-instance-list: "AAAAVgIAAABBRkkAAAAAAAAAAAAAAAAAAAAAYAIAAABBRkMAAAAAAAAAAAAAAAAAAAAAcAIAAABBRkcAAAAAAAAAAAAAAAAA"
                 aft-params: [
-                  "`"
-                  "p"
+                  " "
+                  ","
+                  "4"
+                  "<"
+                  "@"
+                  "D"
+                  "L"
+                  "P"
+                  "T"
+                  "X"
                 ]
-                enable_stop_clocks: "AAAo1AAAAAAAEAAAAAAAAAAAAAAAAACAAQABAAAAAAD/////AAAAAAAAAAAAAAAAAAA81AAAAAAEBgAAAAAAAAAAAAAAAACAAQAAAAAAAAAAAwAAAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAAACONQAAAAAVAAAAAAAAABAAAAAAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAABAONQAAAAAAEAAAAAAAAA0BT8AAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAAADONQAAAAAGAAAAAAAAAAEAAAAAAAAgAEAAAAAAAAA"
+                enable_stop_clocks: "AAAo+AAAAAAAAQAAAAAAAAAAAAAAAACADwAPAAAAAAD/////AAAAAAAAAAAAAAAAAACM+QAAAAAEBgAAAAAAAAAAAAAAAACAAQAAAAAAAAAAAwAAAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAAACiPkAAAAAVAAAAAAAAABAAAAAAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAABAiPkAAAAAAEAAAAAAAAA0BT8AAAAAgAEAAAAAAAAA/////wAAAAAAAAAAAAAAAAADiPkAAAAAGAAAAAAAAAAEAAAAAAAAgAEAAAAAAAAA"
               }
             }
             {
               aod2: {
+                function-aod_swclk_tahiti: [
+                  "'"
+                  "OIPGh"
+                ]
+                function-aod_swdio_tahiti: [
+                  "'"
+                  "OIPGg"
+                ]
-                AAPL,phandle: 280
+                AAPL,phandle: 321
                 function-aod_swclk: [
-                  "("
-                  "OIPGG"
+                  "'"
+                  "OIPGg"
                 ]
                 function-aod_swdio: [
-                  "("
-                  "OIPGF"
+                  "'"
+                  "OIPGH"
                 ]
               }
             }
             {
               aod3: {
-                AAPL,phandle: 281
+                AAPL,phandle: 322
                 function-aod_swclk: [
-                  "("
-                  "OIPGc"
+                  "T"
                 ]
                 function-aod_swdio: [
-                  "("
+                  "T"
                 ]
               }
             }
             {
               pearl-sep: {
-                AAPL,phandle: 282
+                AAPL,phandle: 324
-                clock-gates: 425
+                clock-gates: 296
               }
             }
             {
               haptics-support-interface: {
-                AAPL,phandle: 283
+                AAPL,phandle: 325
               }
             }
             {
               event-log-handler: {
-                AAPL,phandle: 45
+                AAPL,phandle: 44
-                event-logs: "AAAAAAAAAAC4gAMAAAAAAAAAAAAAYAcAAQAAAAEAAAA8wgMAAgAAAAIAAAAEwAYAAwAAAAMAAAAAgAcABAAAAAQAAADwPwAABQAAAAUAAADwPwAABgAAAAYAAADwDwAABwAAAAcAAAAAKgAACAAAAAgAAADwDwAA"
+                event-logs: "AAAAAAAAAACwgAMAAAAAAAAAAAAAYAcAAQAAAAEAAABcwgMAAgAAAAIAAAAEwAYAAwAAAAMAAAAAgAcABAAAAAQAAADwPwAABQAAAAUAAADwDwAABgAAAAYAAAAAKgAABwAAAAcAAADwDwAACAAAAAgAAADEmAoACAAAAAkAAAAAAgAA"
                 interrupts: [
-                  "!"
-                  "\""
+                  "%"
+                  "&"
                 ]
                 reg: [
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
+                  {
+                    addr: 8347090944
+                    size: 32768
+                  }
                   {
-                    addr: 3559391232
+                    addr: 4163371008
                   }
                   {
-                    addr: 3221225472
+                    addr: 4026531840
                   }
                   {
-                    addr: 3558866944
+                    addr: 4162846720
                   }
                   {
-                    addr: 3223912448
+                    addr: 4029202432
                   }
                   {
-                    addr: 3223896064
+                    addr: 8347156480
                   }
                   {
-                    addr: 3223846912
+                    addr: 4029153280
                   }
                   {
-                    addr: 4320559104
+                    addr: 4069523456
                   }
                   {
-                    addr: 4320362496
+                    addr: 4068474880
-                    size: 32768
+                    size: 770048
                   }
                 ]
               }
             }
             {
               audio-resource-manager: {
-                AAPL,phandle: 284
+                AAPL,phandle: 326
               }
             }
             {
               wlan: {
-                AAPL,phandle: 285
+                AAPL,phandle: 327
-                audio-protection-driver: "AppleCS42L77Audio"
+                audio-protection-driver: "AppleCS42L79Audio"
-                module-instance: "poppy"
+                module-instance: "cephalotus"
               }
             }
             {
               bluetooth: {
-                interrupts: 144115196665790600
+                interrupts-h17a: [
+                  "i"
+                ]
+                interrupts-h17p: [
+                  "j"
+                ]
-                AAPL,phandle: 286
+                AAPL,phandle: 328
-                interrupt-parent: "("
+                interrupt-parent: "'"
               }
             }
             {
               grimaldi: {
-                AAPL,phandle: 287
+                AAPL,phandle: 329
                 function-grimaldi-device-id: [
+                  "D"
                   ...
-                  "Q"
                 ]
                 function-grimaldi-gain: [
-                  "Q"
+                  "D"
                   ...
                 ]
                 function-grimaldi-power-get: [
+                  "D"
                   ...
-                  "Q"
                 ]
                 function-grimaldi-power-set: [
-                  "Q"
+                  "D"
                   ...
                 ]
               }
             }
             {
               gpio-canary: {
-                AAPL,phandle: 288
+                AAPL,phandle: 330
               }
             }
             {
               apple-processor-trace: {
-                AAPL,phandle: 289
+                AAPL,phandle: 332
-                compatible: "apple-processor-trace,t8130"
+                compatible: "apple-processor-trace,t8140"
               }
             }
+            {
+              aem: {
+                AAPL,phandle: 79
+                children: [
+                ]
+                compatible: "iop,secure-rtbuddy-proxy"
+                exclave-assigned: null
+                exclave-edk-endpoint: 14
+                exclave-endpoint: 10
+                interrupt-parent: " "
+                interrupts: 1692217115021
+                iommu-parent: "H"
+                role: "AOP-EXCLAVE"
+              }
+            }
+            {
+              aop-exclave-ioreporting: {
+                AAPL,phandle: 80
+                children: [
+                ]
+                compatible: "iop,secure-rtbuddy-ioreporting"
+                exclave-assigned: null
+                exclave-endpoint: "M"
+                interrupt-parent: " "
+                role: "AOP-EXCLAVE"
+              }
+            }
+            {
+              aop2: {
+                AAPL,phandle: 81
+                children: [
+                  {
+                    iop-aop2-nub: {
+                      AAPL,phandle: 82
+                      children: [
+                      ]
+                      compatible: "iop-nub,rtbuddy-v2"
+                      no-firmware-service: null
+                      no-shutdown: 1
+                      watchdog-enable: null
+                    }
+                  }
+                ]
+                clock-gates: null
+                clock-ids: null
+                compatible: "iop,ascwrap-v6"
+                device_type: "aop2"
+                idle-ctrl-check: null
+                interrupt-parent: " "
+                interrupts: "jwEAAI4BAACRAQAAkAEAAA=="
+                iommu-parent: "I"
+                iop-version: 1
+                power-gates: null
+                reg: [
+                  {
+                    addr: 4318035968
+                    size: 557056
+                  }
+                  {
+                    addr: 4312072192
+                    size: 16384
+                  }
+                  {
+                    addr: 4318216192
+                    size: 245768
+                  }
+                ]
+                role: "AOP2"
+              }
+            }
+            {
+              esm: {
+                AAPL,phandle: 101
+                children: [
+                ]
+                compatible: "iop,exclave-sep-manager"
+                exclave-assigned: null
+                exclave-edk-endpoint: 18
+                exclave-endpoint: 17
+                interrupt-parent: " "
+                interrupts: 1490353652062
+                iommu-parent: "d"
+              }
+            }
             {
               aes: {
-                AAPL,phandle: 46
+                AAPL,phandle: 45
-                clock-gates: "C"
+                clock-gates: "K"
-                interrupts: 878
+                interrupts: 1107
-                iommu-parent: "l"
+                iommu-parent: "k"
                 reg: [
                   {
-                    addr: 2499854336
+                    addr: 6257950720
                   }
                   {
-                    addr: 3559768064
+                    addr: 4163747840
                   }
                   {
-                    addr: 3557261312
+                    addr: 4161241088
                   }
                 ]
               }
             }
+            {
+              dcp-exclave-mailbox: {
+                AAPL,phandle: 193
+                children: [
+                ]
+                compatible: "iop,secure-rtbuddy-proxy"
+                exclave-assigned: null
+                exclave-edk-endpoint: 15
+                exclave-endpoint: 11
+                interrupt-parent: " "
+                interrupts: 2933462663854
+                iommu-parent: 184
+                role: "DCP-EXCLAVE"
+              }
+            }
+            {
+              dcp-exclave-ioreporting: {
+                AAPL,phandle: 194
+                children: [
+                ]
+                compatible: "iop,secure-rtbuddy-ioreporting"
+                exclave-assigned: null
+                exclave-endpoint: "N"
+                interrupt-parent: " "
+                role: "DCP-EXCLAVE"
+              }
+            }
+            {
+              exdisplaypipe: {
+                AAPL,phandle: 195
+                children: [
+                ]
+                compatible: "exdisplaypipe,t8140"
+                device_type: "exdisplaypipe"
+                exclave-assigned: null
+                exclave-edk-endpoint: 29
+                exclave-endpoint: 28
+                interrupt-parent: " "
+                interrupts: "4wIAAOQCAADlAgAAswIAAA=="
+                iommu-parent: 811748819132
+                tunable-target: "TDispTarget93"
+              }
+            }
+            {
+              jpeg0-h17a: {
+                AAPL,phandle: 211
+                children: [
+                ]
+                clock-gates: "JAEAAPwAAAD9AAAA"
+                clock-ids: 1387274436930
+                compatible: [
+                  "jpeg,t8101"
+                  "jpeg,s5l8920x"
+                ]
+                coprovider-group: "jpeg"
+                device_type: "jpeg"
+                hw-type: "110008"
+                interrupt-parent: " "
+                interrupts: 1040
+                iommu-parent: 214
+                power-gates: "JAEAAPwAAAD9AAAA"
+                reg: {
+                  addr: 2097152000
+                  size: 16384
+                }
+              }
+            }
+            {
+              jpeg1-h17a: {
+                AAPL,phandle: 212
+                children: [
+                ]
+                clock-gates: "JQEAAPwAAAD9AAAA"
+                clock-ids: 1387274436930
+                compatible: [
+                  "jpeg,t8101"
+                  "jpeg,s5l8920x"
+                ]
+                coprovider-group: "jpeg"
+                device_type: "jpeg"
+                hw-type: "110008"
+                interrupt-parent: " "
+                interrupts: 1043
+                iommu-parent: 215
+                power-gates: "JQEAAPwAAAD9AAAA"
+                reg: {
+                  addr: 2097545216
+                  size: 16384
+                }
+              }
+            }
+            {
+              dart-jpeg-h17a: {
+                AAPL,phandle: 213
+                children: [
+                  {
+                    mapper-jpeg0-h17a: {
+                      AAPL,phandle: 214
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 0
+                      tail-padding: 1
+                    }
+                  }
+                  {
+                    mapper-jpeg1-h17a: {
+                      AAPL,phandle: 215
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 1
+                      tail-padding: 1
+                    }
+                  }
+                ]
+                compatible: "dart,t8110"
+                dart-options: "%"
+                device_type: "dart"
+                flush-by-dva: 1
+                instance: [
+                  "TRAD"
+                  "DART"
+                ]
+                interrupt-parent: " "
+                interrupts: 1041
+                page-size: 16384
+                reg: {
+                  addr: 2097283072
+                  size: 49152
+                }
+                sid: 4294967296
+                sid-count: 2
+                vm-base: 1099511627776
+                vm-size: 3298534883328
+              }
+            }
+            {
+              jpeg0-h17p: {
+                AAPL,phandle: 216
+                children: [
+                ]
+                clock-gates: "JAEAAPwAAAD9AAAA"
+                clock-ids: 1387274436930
+                compatible: [
+                  "jpeg,t8101"
+                  "jpeg,s5l8920x"
+                ]
+                coprovider-group: "jpeg"
+                device_type: "jpeg"
+                hw-type: "110000"
+                interrupt-parent: " "
+                interrupts: 1040
+                iommu-parent: 219
+                power-gates: "JAEAAPwAAAD9AAAA"
+                reg: {
+                  addr: 2097152000
+                  size: 16384
+                }
+              }
+            }
+            {
+              jpeg1-h17p: {
+                AAPL,phandle: 217
+                children: [
+                ]
+                clock-gates: "JQEAAPwAAAD9AAAA"
+                clock-ids: 1387274436930
+                compatible: [
+                  "jpeg,t8101"
+                  "jpeg,s5l8920x"
+                ]
+                coprovider-group: "jpeg"
+                device_type: "jpeg"
+                hw-type: "110000"
+                interrupt-parent: " "
+                interrupts: 1043
+                iommu-parent: 221
+                power-gates: "JQEAAPwAAAD9AAAA"
+                reg: {
+                  addr: 2097545216
+                  size: 16384
+                }
+              }
+            }
+            {
+              dart-jpeg0-h17p: {
+                AAPL,phandle: 218
+                children: [
+                  {
+                    mapper-jpeg0-h17p: {
+                      AAPL,phandle: 219
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 0
+                    }
+                  }
+                ]
+                compatible: "dart,t8110"
+                dart-options: "%"
+                device_type: "dart"
+                flush-by-dva: 1
+                instance: [
+                  "TRAD"
+                  "DART"
+                ]
+                interrupt-parent: " "
+                interrupts: 1041
+                page-size: 16384
+                reg: {
+                  addr: 2097283072
+                  size: 49152
+                }
+                sid: 0
+                sid-count: 1
+                vm-base: 1099511627776
+                vm-size: 3298534883328
+              }
+            }
+            {
+              dart-jpeg1-h17p: {
+                AAPL,phandle: 220
+                children: [
+                  {
+                    mapper-jpeg1-h17p: {
+                      AAPL,phandle: 221
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 0
+                    }
+                  }
+                ]
+                compatible: "dart,t8110"
+                dart-options: "%"
+                device_type: "dart"
+                flush-by-dva: 1
+                instance: [
+                  "TRAD"
+                  "DART"
+                ]
+                interrupt-parent: " "
+                interrupts: 1044
+                page-size: 16384
+                reg: {
+                  addr: 2097676288
+                  size: 49152
+                }
+                sid: 0
+                sid-count: 1
+                vm-base: 1099511627776
+                vm-size: 3298534883328
+              }
+            }
             {
               aop: {
+                ext-irq-reg-index: 4
-                AAPL,phandle: 47
+                AAPL,phandle: 46
                 children: [
                   {
                     iop-aop-nub: {
+                      no-shutdown: 1
+                      routes: "O"
-                      AAPL,phandle: 48
+                      AAPL,phandle: 47
-                      aop-target: 2
+                      aop-target: 1
                       children: [
                         {
                           cma: {
-                            AAPL,phandle: 49
+                            AAPL,phandle: 69
-                            coex0-driver-name: "AppleAOPHaptics"
+                            coex0-driver-name: "IOPHaptics"
                           }
                         }
                         ...
                         {
                           aop-audio: {
                             children: [
-                              {
-                                audio-codecmclkmgr: {
-                                  AAPL,phandle: 60
-                                  children: [
-                                  ]
-                                  compatible: "aop-audio-control"
-                                  device_type: "aop-audio-control"
-                                  identifier: "mmca"
-                                }
-                              }
-                              {
-                                audio-aop-mca3-pmgr: {
-                                  AAPL,phandle: 69
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-mca3-pmgr"
-                                  device_type: "audio-aop-mca3-pmgr"
-                                  identifier: "cp3m"
-                                }
-                              }
-                              {
-                                audio-leap-mca-loopback: {
-                                  AAPL,phandle: 70
-                                  children: [
-                                  ]
-                                  compatible: "audio-leap-mca-loopback"
-                                  device_type: "audio-leap-mca-loopback"
-                                  identifier: "blpl"
-                                }
-                              }
-                              {
-                                audio-lp-mic-in: {
-                                  AAPL,phandle: 71
-                                  children: [
-                                  ]
-                                  clockDomain: "niam"
-                                  compatible: "audio-aop-lp-mic-in"
-                                  device_type: "audio-aop-lp-mic-in"
-                                  function-codec_lpmic: [
-                                    "mplc"
-                                  ]
-                                  identifier: "iapl"
-                                  preferNominalTimestamp: 0
-                                }
-                              }
-                              {
-                                audio-aop-edt-config: {
-                                  AAPL,phandle: 72
-                                  children: [
-                                  ]
-                                  device-ui32-property-list: "IG10YtMAAAAEAAAAIGNyYdMAAAAEAAAAIG10YtQAAAARAAAAIG10YtUAAAD6BwAAIG10YtYAAAALCQYAIG10YtsAAAAFAwAAIG10YtwAAAACBB4AIG10YtcAAAAcAAAAIGNyYdcAAAAcAAAA"
-                                  device_type: "aop-audio-config"
-                                  identifier: "Ctde"
-                                }
-                              }
-                              {
-                                audio-hw-pcm-audiomgr: {
-                                  AAPL,phandle: 73
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-pcmaudiomgr"
-                                  device_type: "audio-hw-pcm-audiomgr"
-                                  identifier: "Mmcp"
-                                  kci-name: "AOPAudioHWPCMAssetManagerInterface"
-                                }
-                              }
-                              {
-                                audio-speaker: {
-                                  AAPL,phandle: 61
-                                  children: [
-                                  ]
-                                  compatible: "aop-audio-speaker"
-                                  device_type: "aop-audio-control"
-                                  identifier: "capa"
-                                }
-                              }
-                              {
-                                audio-hall: {
-                                  AAPL,phandle: 62
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-hall"
-                                  device_type: "audio-aop-hall"
-                                  identifier: "tnks"
-                                }
-                              }
-                              {
-                                aop-ad5860-config: {
-                                  AAPL,phandle: 63
-                                  children: [
-                                  ]
-                                  compatible: "halle-sensor,aop-ad5860-config"
-                                  default-calibration: "HR0kAACHCWsAAAAAAAAAAA=="
-                                  function-access_hall_register: [
-                                    ">"
-                                    " ger"
-                                  ]
-                                  function-get_property: [
-                                    ">"
-                                    "Pteg"
-                                  ]
-                                  function-set_property: [
-                                    ">"
-                                    "Ptes"
-                                  ]
-                                  halle-calibration: "syscfg/PSCl"
-                                  identifier: "Clah"
-                                  override-config: 1
-                                  reg: {
-                                    addr: 10737418240008
-                                  }
-                                  serial-config: 18019896067621120
-                                  slot-config: "BAEBBgEBCAEBCgEBDAABAA=="
-                                }
-                              }
-                              {
-                                audio-haptic-leap: {
-                                  AAPL,phandle: 64
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-haptic-leap"
-                                  device_type: "audio-aop-haptic-leap"
-                                  identifier: "paelwfpl"
-                                  kci-name: "AppleHapticsAudioInterface"
-                                  parking-node-id: "Nkrp"
-                                }
-                              }
-                              {
-                                audio-hapticmgr: {
-                                  AAPL,phandle: 65
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-hapticmgr"
-                                  device_type: "audio-aop-hapticmgr"
-                                  identifier: " hpadhpa"
-                                }
-                              }
-                              {
-                                audio-haptic: {
-                                  AAPL,phandle: 66
-                                  audio-enable-warmup-ms: 3
-                                  children: [
-                                  ]
-                                  compatible: "aop-audio-haptic"
-                                  device_type: "aop-audio-control"
-                                  function-haptics_session: [
-                                    "csph"
-                                  ]
-                                  function-power_peak_budget: [
-                                    "wpkp"
-                                  ]
-                                  function-thermal_budget: [
-                                    "reht"
-                                  ]
-                                  identifier: "chpa"
-                                  input-latency: 8
-                                  output-latency: 8
-                                  parking-timeout-ms: "M"
-                                  peak-power-range: "RBYAADQFAABEFgAA"
-                                  sizeof-zerofilled-buffer: 5
-                                  thermal-budget-range: "PwsAAHYBAAA/CwAA"
-                                }
-                              }
-                              {
-                                audio-hpdbg: {
-                                  AAPL,phandle: 67
-                                  children: [
-                                  ]
-                                  compatible: "aop-audio-hpdbg"
-                                  default-input-data-selectors: "capacaocsopcbqes0Vra0Iraxlahylah"
-                                  device_type: "aop-audio-control"
-                                  function-input-data-selectors: [
-                                    "sidh"
-                                  ]
-                                  identifier: "cdha"
-                                  input-data-selectors: "AAAAAGNhcGFjYW9hc29wYzBJcmEwVnJhY2FvY3N0bGYxY3BoZG1jaHhsYWh0dW9jcnhhaHBtdGNwbXRzMFZwczBJcHN1YXhtanJ0bW5leG0yY3BoM2NwaDRjcGhzcG1zYnFlc25lcG1lcG9hbmVwYW9jZGlpZGRpbWlsdnVhb2F1YXBheWxhaHJ5YWhmZmVjZG1jdnhzZXJ5c2VycG1yc3BtcnBwbXJjZG1jZzBWYXBhZ3BjdGNtc3RjbHNwZGN0b3BjdGNjY3RnbGN0MnZjdG11Y3RhZ3R0cG10eHBtdHlnd2xzZ3RsZnBtcnRmZm9zbmVvdHNvcGN3b3BzZ2NwYXRzZXh0c2V2dHNlYnRuaWJmcGhiMHRzdDF0c3QydHN0M3RzdHFyaWhxcmlhbmV2czF0bmkydG5pdGFidnRzYnYxYnBtMmJwbXhsZnJ4Y2ZmeGxmZnhjZnN0c2ZyY3NwYWNzb2FmdmxpaWcyYWNnMmFpdGNzY3Rjc2l0cnBjdHJwaXZhcGN2YXA1MmFwaXhtcGljYXA1MmNwaXdwc2N3cHNpd3BjY3dwY2l0Y3JjdGNydGNrMXlsZnJ5Y2ZmeWxmZnljZnN0ZzJh"
-                                  input-latency: 5
-                                  output-latency: 5
-                                  sizeof-zerofilled-buffer: 5
-                                }
-                              }
-                              {
-                                audio-aop-mca2-pmgr: {
-                                  AAPL,phandle: 68
-                                  children: [
-                                  ]
-                                  compatible: "audio-aop-mca2-pmgr"
-                                  device_type: "audio-aop-mca2-pmgr"
-                                  identifier: "cp2m"
-                                }
-                              }
                             ]
-                            compatible: "aop-audio"
+                            compatible: "iop-audio,aop-service"
                           }
                         }
                         {
                           smc-control: {
-                            AAPL,phandle: 74
+                            AAPL,phandle: 61
-                            smc-aop-charge-config: "AABE9AIAAAAEAAAAKgAAAA=="
+                            smc-aop-charge-config: "AABkEAMAAAAEAAAAKgAAAA=="
                           }
                         }
                         {
                           aop-smart-cover: {
-                            AAPL,phandle: 75
+                            AAPL,phandle: 62
                           }
                         }
                         {
                           rose: {
+                            function-rose_coredump-pre-p2: [
+                              "S"
+                            ]
-                            AAPL,phandle: 76
+                            AAPL,phandle: 63
                             function-rd_rose_pwr: [
-                              "4RKp8DLr"
-                              "s"
+                              "8RKpDLcp"
+                              "q"
                             ]
                             function-rose_coredump: [
-                              "W"
+                              "S"
                             ]
                             function-rose_pwr: [
-                              "4WKp8DLr"
-                              "s"
+                              "8WKpDLcp"
+                              "q"
                             ]
                             function-rose_reset: [
-                              "4WKp70Pg"
-                              "s"
+                              "8WKpOIcp"
+                              "q"
                             ]
-                            iommu-parent: "V"
+                            iommu-parent: "N"
                           }
                         }
                         {
                           jarvis: {
-                            AAPL,phandle: 77
+                            AAPL,phandle: 64
-                            magnitude-cal: 81920000
+                            magnitude-cal: 49152000
-                            phi-attach-high-cal: -162529
+                            phi-attach-high-cal: -82575
-                            phi-attach-low-cal: 93716
+                            phi-attach-low-cal: 173670
-                            phi-detach-high-cal: 43253
+                            phi-detach-high-cal: 123207
-                            phi-detach-low-cal: -112066
+                            phi-detach-low-cal: -32112
-                            phi-ignore-high-cal: 177602
+                            phi-ignore-high-cal: 163840
-                            phi-ignore-low-cal: 28835
+                            phi-ignore-low-cal: 42598
-                            std-dev-x-cal: 11010048
+                            std-dev-x-cal: 6684672
-                            std-dev-y-cal: 7995392
+                            std-dev-y-cal: 5701632
-                            std-dev-z-cal: 9502720
+                            std-dev-z-cal: 4194304
-                            theta-attach-high-cal: 167116
+                            theta-attach-high-cal: 131727
-                            theta-detach-low-cal: 38666
+                            theta-detach-low-cal: 74055
                           }
                         }
                         {
                           als: {
-                            clk-freq-async: 32768
-                            clk-freq-sync: 345600
-                            digitizer-filter-window-type: 1
-                            freq: "x"
-                            sync2-1p2v-en: 1
-                            sync2-lower-freq-range-en: 0
-                            tint-time-async: 5
-                            tint-time-sync: "4"
-                            use-prox-for-occlusion: 0
+                            supports-float-lux: 1
-                            AAPL,phandle: 78
+                            AAPL,phandle: 65
-                            hotspot-center-x: 136059289
+                            hotspot-center-x: 133811404
-                            hotspot-center-y: 164528128
+                            hotspot-center-y: 35977953
                           }
                         }
                         {
                           gnss: {
-                            AAPL,phandle: 79
+                            AAPL,phandle: 66
                             function-gnss-time-mark: [
                               ...
-                              "W"
+                              "S"
                             ]
                           }
                         }
                         {
                           dcp-control: {
-                            AAPL,phandle: 80
+                            AAPL,phandle: 67
                           }
                         }
                         {
                           grimaldi-control: {
-                            function-grimaldi-power: [
-                              "s"
-                              "4WKpaDLr"
-                            ]
+                            function-flicker_bias: [
+                              "sblf"
+                            ]
-                            AAPL,phandle: 81
+                            AAPL,phandle: 68
                           }
                         }
                         {
                           accel: {
-                            accel-nominal-extr-cal: "syscfg/ARXN"
+                            accel-nominal-extr-cal: "syscfg/ARXN,hex/02000101000000002800000001000000000000000000FFFF0000000000000100000000000000000000000000000000000000FFFF2A08927F"
-                            accel-range-intr-cal: "syscfg/ARNC"
+                            accel-range-intr-cal: "syscfg/ARNC,hex/03000101000000002C000000020000002000000000007A3F00000000000000000000000000007A3F00000000000000000000000000007A3F5CCD7FA3"
                           }
                         }
+                        {
+                          aop-pio-filters: {
+                            AAPL,phandle: 48
+                            children: [
+                            ]
+                            pio-dst-filt-fr-global: 0
+                            pio-dst-filt-global: 0
+                            pio-src-filt-global: 2
+                          }
+                        }
+                        {
+                          aop-scm-xbar-d9x: {
+                            AAPL,phandle: 49
+                            children: [
+                            ]
+                            gpio-to-scm-muxsel: [
+                              "0"
+                            ]
+                            gpio-to-scm-muxsel-p1: [
+                              "d"
+                              "("
+                            ]
+                            gpio-to-scm-muxsel-por: [
+                              "d"
+                              "("
+                            ]
+                            scm-to-gpio-muxsel: [
+                              "$"
+                              "0"
+                            ]
+                            scm-to-gpio-muxsel-p1: [
+                              " "
+                              "("
+                              "3"
+                            ]
+                            scm-to-gpio-muxsel-por: [
+                              "H"
+                              " "
+                              "d"
+                              "3"
+                            ]
+                          }
+                        }
+                        {
+                          aop-voicetrigger: {
+                            AAPL,phandle: 60
+                            children: [
+                            ]
+                            compatible: "iop-audio,aop-service"
+                            device_type: "aop-voicetrigger"
+                            name-override: "AOPVoiceTriggerService"
+                          }
+                        }
                         {
                           hgaccel: {
-                            accel-nominal-extr-cal: "syscfg/ARXN"
+                            accel-nominal-extr-cal: "syscfg/AhXN,hex/01000101000000002800000001000000000000000000FFFF0000000000000100000000000000000000000000000000000000FFFF3D0CC7C5"
                           }
                         }
                         {
                           gyro: {
-                            gyro-nominal-extr-cal: "syscfg/GRXN"
+                            gyro-nominal-extr-cal: "syscfg/GRXN,hex/020001010000000028000000010000000000000000000100000000000000FFFF00000000000000000000000000000000000001001291BE7F"
-                            gyro-range-intr-cal: "syscfg/GRNC"
+                            gyro-range-intr-cal: "syscfg/GRNC,hex/03000101000000002C00000002000000A00F00000000FA390000000000000000000000000000FA390000000000000000000000000000FA39B96DC7D9"
                           }
                         }
                         {
                           compass: {
-                            coex0-driver-name: "AppleCS35L27Amp"
+                            coex0-driver-name: "IOPAudioSpeaker"
-                            compass-apl-compensation-lgd: "syscfg/MDCC,hex/010000000601000035FFFFFFD1020000"
+                            compass-apl-compensation-lgd: "syscfg/MDCC,hex/01000000DF000000A4FFFFFFEC000000"
-                            compass-apl-compensation-sdc: "syscfg/MDCC,hex/01000000AA010000E6FEFFFF4FFFFFFF"
+                            compass-apl-compensation-sdc: "syscfg/MDCC,hex/01000000EC000000A4FFFFFFE5000000"
-                            compass-temp-calibration: "AwAAABQuAAB71P//rgcBAOX////s////2f///wAAAAA="
+                            compass-temp-calibration: "AwAAAIEVAABv8v//SKEAAND////D////pP///wAAFAA="
-                            compass-vbus-compensation: "syscfg/CVCC,hex/010000004E010000A4FFFFFF0B000000"
+                            compass-vbus-compensation: "syscfg/CVCC,hex/01000000B60300004A000000B2000000"
-                            compass-wallet-compensation: "AQAAAL8NAQCw6///IQAAAFbr//9t4AAA0AAAAGQJAAClFwAArP8AAA=="
+                            compass-wallet-compensation: ">"
                           }
                         }
                         {
                           compass_1: {
-                            compass-orientation: "syscfg/JRot,hex/01000101010000002800000003000000D5770000C61DFFFF000000003AE20000D577000000000000000000000000000000000100673CC654"
+                            compass-orientation: "syscfg/JRot,hex/010001010100000028000000030000000000010000000000000000000000000000000100000000000000000000000000000001004b9528a4"
                           }
                         }
                         {
                           pressure: {
+                            pressure-global-offset-cal: 5376
                           }
                         }
                         {
                           spherecontrol: {
-                            isp-aop-control-config: "AIBE9AIAAABAAAAAPgAAAA=="
+                            isp-aop-control-config: "AIBkEAMAAABAAAAAPgAAAA=="
-                            isp-aop-motion-config: "AIBE9AIAAACAAAAAPwAAAA=="
+                            isp-aop-motion-config: "AIBkEAMAAACAAAAAPwAAAA=="
-                            isp-aop-motion_full_rate-config: "AIBE9AIAAAAQAAAAPAAAAA=="
+                            isp-aop-motion_full_rate-config: "AIBkEAMAAAAQAAAAPAAAAA=="
-                            isp-aop-pearl-config: "AIBE9AIAAAAgAAAAPQAAAA=="
+                            isp-aop-pearl-config: "AIBkEAMAAAAgAAAAPQAAAA=="
                           }
                         }
                         ...
                       ]
-                      firmware-name: "iphone16aop"
+                      firmware-name: "iphone17aop"
-                      region-base: 12696158208
+                      region-base: 13165920256
                     }
                   }
                 ]
-                interrupts: "gAEAAH8BAACCAQAAgQEAAA=="
+                interrupts: "hwEAAIYBAACJAQAAiAEAAA=="
-                iommu-parent: "S"
+                iommu-parent: "G"
                 reg: [
                   {
-                    addr: 3829399552
+                    addr: 4301258752
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 3825532928
+                    addr: 4295294976
                   }
                   {
-                    addr: 3837788160
+                    addr: 4307550208
                   }
                   {
-                    addr: 3559555072
+                    addr: 4163534848
                   }
+                  {
+                    addr: 4301438976
+                    size: 245768
+                  }
                 ]
               }
             }
+            {
+              isp-exclave-proxy: {
+                AAPL,phandle: 232
+                children: [
+                ]
+                compatible: "isp,isp-exclave-proxy"
+                device_type: "isp"
+                exclave-assigned: null
+                exclave-edk-endpoint: 24
+                exclave-endpoint: 23
+              }
+            }
+            {
+              ave1: {
+                AAPL,phandle: 236
+                children: [
+                ]
+                clock-gates: [
+                  "}"
+                  "~"
+                  "|"
+                ]
+                clock-ids: 418
+                compatible: "ave2"
+                coprovider-group: "ave"
+                device_type: "ave"
+                function-clock_req_interrupt: [
+                  "\""
+                  "QRIC3"
+                  "#"
+                ]
+                function-mcc_dataset: [
+                  "("
+                  "SD$M"
+                ]
+                interrupt-parent: " "
+                interrupts: "ygMAAMQDAADDAwAAxgMAAMUDAAA="
+                iommu-parent: 238
+                power-gates: [
+                  "}"
+                  "~"
+                  "|"
+                ]
+                reg: [
+                  {
+                    addr: 2031091712
+                    size: 4571136
+                  }
+                  {
+                    addr: 2038431744
+                    size: 8388608
+                  }
+                  {
+                    addr: 2030370816
+                    size: 16384
+                  }
+                  {
+                    addr: 4033904680
+                    size: 16384
+                  }
+                  {
+                    addr: 2013265920
+                    size: 16777216
+                  }
+                ]
+                soc-id: "t8140"
+                sve-id: 1
+              }
+            }
+            {
+              admac-base-s: {
+                #dma-channels: 13
+                #skip-channels-rx: 2
+                #skip-channels-tx: 1
+                AAPL,phandle: 298
+                channel-buffer-alloc-base-rx: 0
+                channel-buffer-alloc-base-tx: 0
+                channel-buffer-allocation: "AAIAAAAAAAAAQAAAAAAAAA=="
+                channels-offset: 0
+                children: [
+                ]
+                clock-gates: 299
+                compatible: "admac,t8140"
+                device_type: "admac"
+                interrupt-parent: " "
+                interrupts: 448
+                iommu-parent: null
+                irq-destination-index: 0
+                irq-destinations: " CIAUPCA NTGDSNU"
+                reg: [
+                  {
+                    addr: 4352638976
+                    size: 212992
+                  }
+                  {
+                    addr: 4163534848
+                    size: 8
+                  }
+                ]
+                role: "SSAB"
+                service-exclave_proxy: "DMAChannelProxy@admac-base-s-proxy"
+                skip-channels-rx: 51539607553
+                skip-channels-tx: 12
+              }
+            }
+            {
+              admac-base-s-proxy: {
+                AAPL,phandle: 299
+                children: [
+                ]
+                device_type: "admac-proxy"
+                dma-channel: 4
+                exclave-assigned: null
+                exclave-edk-endpoint: 16
+                exclave-endpoint: 7
+                function-iommu_handler: [
+                  "rpds"
+                ]
+                use-case: "iaph"
+              }
+            }
+            {
+              audio-hp-proxy: {
+                AAPL,phandle: 300
+                children: [
+                ]
+                compatible: "iisaudio,isolated-stream-proxy"
+                device_type: "iis-ec-proxy"
+                exclave-assigned: null
+                exclave-edk-endpoint: "\""
+                exclave-endpoint: "!"
+                identifier: "iaph"
+                physical-descriptions: "4D0AAIC7AABtY3BsBAAAABAAAAAYBAAA"
+              }
+            }
+            {
+              audio-shared-dart-proxy: {
+                AAPL,phandle: 301
+                children: [
+                ]
+                exclave-assigned: null
+                exclave-edk-endpoint: "U"
+                exclave-endpoint: "T"
+                iommu-parent: "M"
+                usecase-dart-map: [
+                  "iaph"
+                  "xpda"
+                ]
+              }
+            }
+            {
+              dart-apcie2: {
+                AAPL,phandle: 316
+                bypass-16: null
+                children: [
+                  {
+                    mapper-apcie2-wlan: {
+                      AAPL,phandle: 317
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                    }
+                  }
+                  {
+                    mapper-apcie2-bt: {
+                      AAPL,phandle: 318
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                    }
+                  }
+                ]
+                compatible: "dart,t8110"
+                dart-options: "7"
+                device_type: "dart"
+                instance: [
+                  "TRAD"
+                  "DART"
+                ]
+                interrupt-parent: " "
+                interrupts: 1224
+                manual-availability: 1
+                page-size: 16384
+                protection-granularity: 128
+                reg: {
+                  addr: 15334375424
+                  size: 131072
+                }
+                sid: 16
+                sid-count: 17
+                vm-base: 1099512676352
+                vm-offset: "AAAAAAAAAAAAAAAIAAAAAA=="
+                vm-size: 1071644672
+              }
+            }
+            {
+              aod4: {
+                AAPL,phandle: 323
+                children: [
+                ]
+                compatible: [
+                  "aod,t8101"
+                  "aod,s5l8960x"
+                ]
+                default-tck: "d"
+                device_type: "aod"
+                function-aod_swclk: [
+                  "'"
+                  "OIPGV"
+                ]
+                function-aod_swdio: [
+                  "'"
+                  "OIPGU"
+                ]
+                probe-port: 7884
+              }
+            }
+            {
+              sapt: {
+                AAPL,phandle: 331
+                apf: [
+                  "("
+                  "<"
+                  "="
+                  "1"
+                  "1"
+                  "1"
+                  "1"
+                  "1"
+                ]
+                children: [
+                ]
+                policy: 0
+              }
+            }
             {
               dart-aop: {
-                dapf-instance-0: "BAAk5AIAAABzAyTkAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACARpkCAAAAA4BGmQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQCjkAgAAAAtBKOQCAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAgMEp5AIAAACbwynkAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAK+QCAAAAV0gr5AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAAC3kAgAAABMBLeQCAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAABE7AIAAAADAETsAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAH+QCAAAASwwf5AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAQQcGOAgAAAB9IwY4CAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIDFjgIAAAADgMWOAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBABDBQPoCAAAAH8hA+gIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAAET6AgAAAAMARPoCAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAAAC5AIAAAD/PwLkAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAAuQCAAAA/38C5AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQA="
-                error-reflector: 11938037760
-                flush-by-dva: 1
+                allow-dram-apf-slices-0: 0
+                always-on: null
+                bypass-12: null
+                exclave-sid: "AQAAAAsAAAAJAAAA"
+                manual-availability: 1
+                vm-base-1: 2199023255552
+                vm-base-9: 1100585369600
+                vm-size-1: 137438953472
+                vm-size-9: 4294901760
-                AAPL,phandle: 82
+                AAPL,phandle: 70
                 children: [
                   {
                     mapper-aop: {
-                      AAPL,phandle: 83
+                      AAPL,phandle: 71
                     }
                   }
                   {
-                    mapper-aop-audio-admac: {
-                      AAPL,phandle: 84
-                      allow-subpage-mapping: null
-                      children: [
-                      ]
-                      compatible: "iommu-mapper"
-                      device_type: "dart-mapper"
-                      reg: 10
-                    }
+                    mapper-exclave-aop: {
+                      AAPL,phandle: 72
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 1
+                    }
                   }
                   {
-                    mapper-aop-base-admac: {
-                      AAPL,phandle: 85
-                      allow-subpage-mapping: null
-                      children: [
-                      ]
-                      compatible: "iommu-mapper"
-                      device_type: "dart-mapper"
-                      reg: 9
-                    }
+                    mapper-aop2: {
+                      AAPL,phandle: 73
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 16
+                    }
                   }
                   {
                     mapper-scm: {
-                      AAPL,phandle: 86
+                      AAPL,phandle: 78
-                      reg: 1
+                      reg: 3
                     }
                   }
+                  {
+                    mapper-admac-leap-s: {
+                      AAPL,phandle: 74
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 11
+                    }
+                  }
+                  {
+                    mapper-admac-base-ns: {
+                      AAPL,phandle: 75
+                      allow-subpage-mapping: null
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 8
+                    }
+                  }
+                  {
+                    mapper-admac-leap-ns: {
+                      AAPL,phandle: 76
+                      allow-subpage-mapping: null
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 10
+                    }
+                  }
+                  {
+                    mapper-admac-base-s: {
+                      AAPL,phandle: 77
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 9
+                    }
+                  }
                 ]
-                dart-options: "%"
+                dart-options: "e"
                 instance: [
-                  "DAPF"
                   ...
-                  "FPAD"
                   ...
                 ]
-                interrupts: 408
+                interrupts: 428
-                reg: [
-                  {
-                    addr: 3833692160
-                    size: 16384
-                  }
-                  {
-                    addr: 3833708544
-                    size: 16384
-                  }
-                ]
+                reg: {
+                  addr: 4311482368
+                  size: 49152
+                }
-                sid: "AAAAAAEAAAAJAAAACgAAAA=="
+                sid: "DAAAAAAAAAAQAAAAAwAAAAgAAAAKAAAA"
-                sid-count: 16
+                sid-count: 17
               }
             }
             {
               aop-gpio: {
-                AAPL,phandle: 87
+                AAPL,phandle: 83
-                interrupts: "ZgEAAGcBAABoAQAAaQEAAGoBAABrAQAAbAEAAA=="
+                interrupts: "fAEAAH0BAAB+AQAAfwEAAIABAACBAQAAggEAAA=="
                 reg: {
-                  addr: 3833741312
+                  addr: 4303503360
                 }
               }
             }
             {
               nub-gpio: {
-                AAPL,phandle: 88
+                AAPL,phandle: 84
-                interrupts: "swEAALQBAAC1AQAAtgEAALcBAAC4AQAAuQEAAA=="
+                interrupts: "2QEAANoBAADbAQAA3AEAAN0BAADeAQAA3wEAAA=="
                 reg: {
-                  addr: 3558801408
+                  addr: 4162781184
                 }
               }
             }
             {
               smc-gpio: {
-                AAPL,phandle: 89
+                AAPL,phandle: 85
-                interrupts: "9QEAAPYBAAD3AQAA+AEAAPkBAAD6AQAA+wEAAA=="
+                interrupts: "PAIAAD0CAAA+AgAAPwIAAEACAABBAgAAQgIAAA=="
                 reg: {
-                  addr: 3699507200
+                  addr: 4236378112
                 }
               }
             }
             {
               mtp-gpio: {
-                AAPL,phandle: 90
+                AAPL,phandle: 86
-                interrupts: "hgMAAIcDAACIAwAAiQMAAIoDAACLAwAAjAMAAA=="
+                interrupts: "aAQAAGkEAABqBAAAawQAAGwEAABtBAAAbgQAAA=="
                 reg: {
-                  addr: 3934388224
+                  addr: 4370694144
                 }
               }
             }
             {
               pmp: {
-                wait-for: "AppleMemCacheController"
-                AAPL,phandle: 91
+                AAPL,phandle: 87
                 children: [
                   {
                     iop-pmp-nub: {
-                      ane-fast-af-bw-dvfs-filter: 16777184
-                      ane-fast-af-bw-threshold: "AAAFAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAEAAUAAAAAADAAAAAAAAAABwAFAAAAAAAAAAAAAAAAAC8ABQAAAA=="
-                      ane-fast-dcs-bw-dvfs-filter: 16777184
-                      ane-fast-dcs-bw-threshold: "AAACAAAAAAAAAAAAAAAAAAAACAAAAAAAAAABAAUAAAAAAAwAAAAAAAAABwAFAAAAAAATAAAAAAAAAAsABQAAAAAAAAAAAAAAAAASAAUAAAA="
-                      ane-slow-af-bw-dvfs-filter: 31
-                      ane-slow-af-bw-threshold: "AAAYAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAXAAMAAAAAADAAAAAAAAAAHwADAAAAAAAAAAAAAAAAAC8AAwAAAA=="
-                      ane-slow-dcs-bw-dvfs-filter: 31
-                      ane-slow-dcs-bw-threshold: "AAAJAAAAAAAAAAAAAAAAAAAAEwAAAAAAAAAIAAMAAAAAAB0AAAAAAAAAEgADAAAAAAAhAAAAAAAAABwAAwAAAAAAAAAAAAAAAAAgAAMAAAA="
-                      dcs-bwr-threshold: "zMwFADMzDAAAABEAzMwVAJmZGQA="
-                      dcs-rd-bwr-threshold: "zMwFADMzDAAAABEAzMwVAJmZGQA="
-                      dcs-wr-bwr-threshold: "AIADAMxMBwAzMwoAmRkNAGZmDwA="
-                      disp-rd-bwr-threshold: "mZkJAMzMDAAzMxMA"
-                      disp-wr-bwr-threshold: "mZkJAMzMDAAzMxMA"
-                      dispext-rd-bwr-threshold: "mZkJAMzMDAAzMxMA"
-                      dispext-wr-bwr-threshold: "mZkJAMzMDAAzMxMA"
-                      soc-rd-bwr-threshold: [
-                        "ff&"
-                      ]
-                      soc-wr-bwr-threshold: [
-                        "ff&"
-                      ]
+                      afi-top-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAwAAAA=="
+                      ane-af-bw-dvfs-filter: 1048575
+                      ane-af-bw-threshold: "AAAYAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAXAAMAAAAAADAAAAAAAAAAHwADAAAAAAAAAAAAAAAAAC8AAwAAAAAAGAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAFwADAAAAAAAwAAAAAAAAAB8AAwAAAAAAAAAAAAAAAAAvAAMAAAAAABgAAAAAAAAAAAAAAAAAAAAgAAAAAAAAABcAAwAAAAAAMAAAAAAAAAAfAAMAAAAAAAAAAAAAAAAALwADAAAAAAAYAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAXAAMAAAAAADAAAAAAAAAAHwADAAAAAAAAAAAAAAAAAC8AAwAAAAAAGAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAFwADAAAAAAAwAAAAAAAAAB8AAwAAAAAAAAAAAAAAAAAvAAMAAAAAAAUAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAQABQAAAAAAMAAAAAAAAAAHAAUAAAAAAAAAAAAAAAAALwAFAAAAAAAFAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAEAAUAAAAAADAAAAAAAAAABwAFAAAAAAAAAAAAAAAAAC8ABQAAAAAABQAAAAAAAAAAAAAAAAAAAAgAAAAAAAAABAAFAAAAAAAwAAAAAAAAAAcABQAAAAAAAAAAAAAAAAAvAAUAAAAAAAUAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAQABQAAAAAAMAAAAAAAAAAHAAUAAAAAAAAAAAAAAAAALwAFAAAAAAACAAAAAAAAAAAAAAAAAAAABAAAAAAAAAABAAUAAAAAABgAAAAAAAAAAwAFAAAAAAAAAAAAAAAAABcABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAQAFAAAAAAAYAAAAAAAAAAMABQAAAAAAAAAAAAAAAAAXAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAEABQAAAAAAGAAAAAAAAAADAAUAAAAAAAAAAAAAAAAAFwAFAAAAAAACAAAAAAAAAAAAAAAAAAAABAAAAAAAAAABAAUAAAAAABgAAAAAAAAAAwAFAAAAAAAAAAAAAAAAABcABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAQAFAAAAAAAYAAAAAAAAAAMABQAAAAAAAAAAAAAAAAAXAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAEABQAAAAAAGAAAAAAAAAADAAUAAAAAAAAAAAAAAAAAFwAFAAAA"
+                      ane-dcs-bw-dvfs-filter: 1048575
+                      ane-dcs-bw-threshold: "AAAJAAAAAAAAAAAAAAAAAAAAEgAAAAAAAAAIAAMAAAAAAB0AAAAAAAAAEQADAAAAAADIAAAAAAAAABwAAwAAAAAAAAAAAAAAAADHAAMAAAAAAAkAAAAAAAAAAAAAAAAAAAASAAAAAAAAAAgAAwAAAAAAHQAAAAAAAAARAAMAAAAAAMgAAAAAAAAAHAADAAAAAAAAAAAAAAAAAMcAAwAAAAAACQAAAAAAAAAAAAAAAAAAABIAAAAAAAAACAADAAAAAAAdAAAAAAAAABEAAwAAAAAAyAAAAAAAAAAcAAMAAAAAAAAAAAAAAAAAxwADAAAAAAAJAAAAAAAAAAAAAAAAAAAAEgAAAAAAAAAIAAMAAAAAAB0AAAAAAAAAEQADAAAAAAAnAAAAAAAAABwAAwAAAAAAAAAAAAAAAAAmAAMAAAAAAAkAAAAAAAAAAAAAAAAAAAASAAAAAAAAAAgAAwAAAAAAHQAAAAAAAAARAAMAAAAAACcAAAAAAAAAHAADAAAAAAAAAAAAAAAAACYAAwAAAAAAAgAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAQAFAAAAAAAMAAAAAAAAAAcABQAAAAAAFgAAAAAAAAALAAUAAAAAAAAAAAAAAAAAFQAFAAAAAAACAAAAAAAAAAAAAAAAAAAACAAAAAAAAAABAAUAAAAAAAwAAAAAAAAABwAFAAAAAAAWAAAAAAAAAAsABQAAAAAAAAAAAAAAAAAVAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAEABQAAAAAADAAAAAAAAAAHAAUAAAAAABYAAAAAAAAACwAFAAAAAAAAAAAAAAAAABUABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAQAFAAAAAAAMAAAAAAAAAAcABQAAAAAAFgAAAAAAAAALAAUAAAAAAAAAAAAAAAAAFQAFAAAAAAACAAAAAAAAAAAAAAAAAAAABAAAAAAAAAABAAUAAAAAAAYAAAAAAAAAAwAFAAAAAAALAAAAAAAAAAUABQAAAAAAAAAAAAAAAAAKAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAEABQAAAAAABgAAAAAAAAADAAUAAAAAAAsAAAAAAAAABQAFAAAAAAAAAAAAAAAAAAoABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAQAFAAAAAAAGAAAAAAAAAAMABQAAAAAACwAAAAAAAAAFAAUAAAAAAAAAAAAAAAAACgAFAAAAAAACAAAAAAAAAAAAAAAAAAAABAAAAAAAAAABAAUAAAAAAAYAAAAAAAAAAwAFAAAAAAALAAAAAAAAAAUABQAAAAAAAAAAAAAAAAAKAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAEABQAAAAAABgAAAAAAAAADAAUAAAAAAAsAAAAAAAAABQAFAAAAAAAAAAAAAAAAAAoABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAQAFAAAAAAAGAAAAAAAAAAMABQAAAAAACwAAAAAAAAAFAAUAAAAAAAAAAAAAAAAACgAFAAAA"
+                      dvfs-disp-min-state: 0
+                      soc-ni0-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAwAAAA=="
+                      soc-ni1-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAwAAAA=="
+                      soc-ni2-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAwAAAA=="
-                      AAPL,phandle: 92
+                      AAPL,phandle: 88
-                      agx-af-rd-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAJgAAAAAAAAAAAAAAAAAAADgAAAAAAAAAJQAFAAAAAABMAAAAAAAAADcABQAAAAAAAAAAAAAAAABLAAUAAAAAABYAAAAAAAAAAAAAAAAAAAA4AAAAAAAAABUABQAAAAAASAAAAAAAAAA3AAUAAAAAAAAAAAAAAAAARwAFAAAAAAAWAAAAAAAAAAAAAAAAAAAALAAAAAAAAAAVAAUAAAAAADkAAAAAAAAAKwAFAAAAAAAAAAAAAAAAADgABQAAAAAACAAAAAAAAAAAAAAAAAAAACwAAAAAAAAABwAFAAAAAAA5AAAAAAAAACsABQAAAAAAAAAAAAAAAAA4AAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAEABQAAAAAAOQAAAAAAAAAfAAUAAAAAAAAAAAAAAAAAOAAFAAAAAAACAAAAAAAAAAAAAAAAAAAACgAAAAAAAAABAAUAAAAAADIAAAAAAAAACQAFAAAAAAAAAAAAAAAAADEABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAAsAAAAAAAAAAYABQAAAAAAAAAAAAAAAAArAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAEABQAAAAAAFgAAAAAAAAAGAAUAAAAAAAAAAAAAAAAAFQAFAAAAAAACAAAAAAAAAAAAAAAAAAAABwAAAAAAAAABAAUAAAAAABEAAAAAAAAABgAFAAAAAAAAAAAAAAAAABAABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAARAAAAAAAAAAYABQAAAAAAAAAAAAAAAAAQAAUAAAA="
+                      agx-af-rd-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAMQAAAAAAAAAAAAAAAAAAAEEAAAAAAAAAMAAFAAAAAABiAAAAAAAAAEAABQAAAAAAAAAAAAAAAABhAAUAAAAAACoAAAAAAAAAAAAAAAAAAAA+AAAAAAAAACkABQAAAAAASAAAAAAAAAA9AAUAAAAAAAAAAAAAAAAARwAFAAAAAAAWAAAAAAAAAAAAAAAAAAAAOAAAAAAAAAAVAAUAAAAAAEgAAAAAAAAANwAFAAAAAAAAAAAAAAAAAEcABQAAAAAACAAAAAAAAAAAAAAAAAAAACwAAAAAAAAABwAFAAAAAABIAAAAAAAAACsABQAAAAAAAAAAAAAAAABHAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAEABQAAAAAAOQAAAAAAAAAfAAUAAAAAAAAAAAAAAAAAOAAFAAAAAAACAAAAAAAAAAAAAAAAAAAACgAAAAAAAAABAAUAAAAAADIAAAAAAAAACQAFAAAAAAAAAAAAAAAAADEABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAAsAAAAAAAAAAYABQAAAAAAAAAAAAAAAAArAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAEABQAAAAAAEQAAAAAAAAAGAAUAAAAAAAAAAAAAAAAAEAAFAAAAAAACAAAAAAAAAAAAAAAAAAAABwAAAAAAAAABAAUAAAAAABEAAAAAAAAABgAFAAAAAAAAAAAAAAAAABAABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAARAAAAAAAAAAYABQAAAAAAAAAAAAAAAAAQAAUAAAA="
-                      agx-af-wr-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAJgAAAAAAAAAAAAAAAAAAADgAAAAAAAAAJQAFAAAAAABMAAAAAAAAADcABQAAAAAAAAAAAAAAAABLAAUAAAAAABYAAAAAAAAAAAAAAAAAAAA4AAAAAAAAABUABQAAAAAASAAAAAAAAAA3AAUAAAAAAAAAAAAAAAAARwAFAAAAAAAWAAAAAAAAAAAAAAAAAAAALAAAAAAAAAAVAAUAAAAAADkAAAAAAAAAKwAFAAAAAAAAAAAAAAAAADgABQAAAAAACAAAAAAAAAAAAAAAAAAAACwAAAAAAAAABwAFAAAAAAA5AAAAAAAAACsABQAAAAAAAAAAAAAAAAA4AAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAEABQAAAAAAOQAAAAAAAAAfAAUAAAAAAAAAAAAAAAAAOAAFAAAAAAACAAAAAAAAAAAAAAAAAAAACgAAAAAAAAABAAUAAAAAADIAAAAAAAAACQAFAAAAAAAAAAAAAAAAADEABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAAsAAAAAAAAAAYABQAAAAAAAAAAAAAAAAArAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAEABQAAAAAAFgAAAAAAAAAGAAUAAAAAAAAAAAAAAAAAFQAFAAAAAAACAAAAAAAAAAAAAAAAAAAABwAAAAAAAAABAAUAAAAAABEAAAAAAAAABgAFAAAAAAAAAAAAAAAAABAABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAARAAAAAAAAAAYABQAAAAAAAAAAAAAAAAAQAAUAAAA="
+                      agx-af-wr-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAMQAAAAAAAAAAAAAAAAAAAEEAAAAAAAAAMAAFAAAAAABiAAAAAAAAAEAABQAAAAAAAAAAAAAAAABhAAUAAAAAACoAAAAAAAAAAAAAAAAAAAA+AAAAAAAAACkABQAAAAAASAAAAAAAAAA9AAUAAAAAAAAAAAAAAAAARwAFAAAAAAAWAAAAAAAAAAAAAAAAAAAAOAAAAAAAAAAVAAUAAAAAAEgAAAAAAAAANwAFAAAAAAAAAAAAAAAAAEcABQAAAAAACAAAAAAAAAAAAAAAAAAAACwAAAAAAAAABwAFAAAAAABIAAAAAAAAACsABQAAAAAAAAAAAAAAAABHAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAEABQAAAAAAOQAAAAAAAAAfAAUAAAAAAAAAAAAAAAAAOAAFAAAAAAACAAAAAAAAAAAAAAAAAAAACgAAAAAAAAABAAUAAAAAADIAAAAAAAAACQAFAAAAAAAAAAAAAAAAADEABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAAsAAAAAAAAAAYABQAAAAAAAAAAAAAAAAArAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAEABQAAAAAAEQAAAAAAAAAGAAUAAAAAAAAAAAAAAAAAEAAFAAAAAAACAAAAAAAAAAAAAAAAAAAABwAAAAAAAAABAAUAAAAAABEAAAAAAAAABgAFAAAAAAAAAAAAAAAAABAABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAQAFAAAAAAARAAAAAAAAAAYABQAAAAAAAAAAAAAAAAAQAAUAAAA="
-                      agx-dcs-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAUAAAAAAAoAAAAAAAAAAAAAAAAAAAAVAAAAAAAAAAkABQAAAAAAHAAAAAAAAAAUAAUAAAAAACUAAAAAAAAAGwAFAAAAAAAAAAAAAAAAACQABQAAAAAABAAAAAAAAAAAAAAAAAAAABUAAAAAAAAAAwAFAAAAAAAcAAAAAAAAABQABQAAAAAAJAAAAAAAAAAbAAUAAAAAAAAAAAAAAAAAIwAFAAAAAAAEAAAAAAAAAAAAAAAAAAAAFQAAAAAAAAADAAUAAAAAABwAAAAAAAAAFAAFAAAAAAAkAAAAAAAAABsABQAAAAAAAAAAAAAAAAAjAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAEABQAAAAAAHAAAAAAAAAAJAAUAAAAAACQAAAAAAAAAGwAFAAAAAAAAAAAAAAAAACMABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAQAFAAAAAAAKAAAAAAAAAAEABQAAAAAAEgAAAAAAAAAJAAUAAAAAAAAAAAAAAAAAEQAFAAAAAAACAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAABAAUAAAAAAAQAAAAAAAAAAQAFAAAAAAAKAAAAAAAAAAMABQAAAAAAAAAAAAAAAAAJAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAEABQAAAAAAAgAAAAAAAAABAAUAAAAAAAgAAAAAAAAAAQAFAAAAAAAAAAAAAAAAAAcABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAQAFAAAAAAACAAAAAAAAAAEABQAAAAAAAgAAAAAAAAABAAUAAAAAAAAAAAAAAAAAAQAFAAAAAAACAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAABAAUAAAAAAAIAAAAAAAAAAQAFAAAAAAACAAAAAAAAAAEABQAAAAAAAAAAAAAAAAABAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAEABQAAAAAAAgAAAAAAAAABAAUAAAAAAAIAAAAAAAAAAQAFAAAAAAAAAAAAAAAAAAEABQAAAA=="
+                      agx-dcs-bw-threshold: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAUAAAAAAAoAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAkAAAAAAAAAHQAAAAAAAAATAAAAAAAAAMgAAAAAAAAAHAAAAAAAAAAAAAAAAAAAAMcAAAAAAAAABAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAwAFAAAAAAAdAAAAAAAAABMABQAAAAAAyAAAAAAAAAAcAAUAAAAAAAAAAAAAAAAAxwAFAAAAAAAEAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAADAAUAAAAAAB0AAAAAAAAAEwAFAAAAAADIAAAAAAAAABwABQAAAAAAAAAAAAAAAADHAAUAAAAAAAIAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAEABQAAAAAAHQAAAAAAAAAJAAUAAAAAACwAAAAAAAAAHAAFAAAAAAAAAAAAAAAAACsABQAAAAAAAgAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAQAFAAAAAAAKAAAAAAAAAAEABQAAAAAAIwAAAAAAAAAJAAUAAAAAAAAAAAAAAAAAIgAFAAAAAAACAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAABAAUAAAAAAAQAAAAAAAAAAQAFAAAAAAAZAAAAAAAAAAMABQAAAAAAAAAAAAAAAAAYAAUAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAABQAAAAAAAQAAAAAAAAAAAAUAAAAAAAkAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAgABQAAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAFAAAAAAABAAAAAAAAAAAABQAAAAAAAQAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAFAAAAAAABAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAUAAAAAAAEAAAAAAAAAAAAFAAAAAAABAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAUAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAABQAAAAAAAQAAAAAAAAAAAAUAAAAAAAEAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAABQAAAA=="
                       controller: [
                         ...
+                        "AFI-TOP-BW"
                         ...
                         ...
                         ...
                         ...
                         ...
-                        "ANE-FAST-AF-BW"
-                        "ANE-FAST-DCS-BW"
-                        "ANE-SLOW-AF-BW"
-                        "ANE-SLOW-DCS-BW"
+                        "ANE-AF-BW"
+                        "ANE-DCS-BW"
                         ...
                         ...
                         ...
-                        "DCS-BWR"
-                        "DCS-RD-BWR"
                         ...
-                        "DCS-WR-BWR"
                         ...
-                        "DISP-RD-BWR"
-                        "DISP-WR-BWR"
-                        "DISPEXT-RD-BWR"
-                        "DISPEXT-WR-BWR"
                         ...
                         ...
                         ...
-                        "SOC-RD-BWR"
-                        "SOC-WR-BWR"
+                        "SOC-NI0-BW"
+                        "SOC-NI1-BW"
+                        "SOC-NI2-BW"
                       ]
-                      dcs-bw-threshold: [
-                        "f&%"
-                        "f&$"
-                      ]
+                      dcs-bw-threshold: "M/MJAAEAAAAAAAAAAAAAADPzEwACAAAAM/MIAAAAAABw/RwAAwAAADPzEgAAAAAAHoUrAAQAAABw/RsAAAAAAAAAAAAAAAAAHoUqAAAAAAA="
-                      firmware-name: "t8130pmp"
+                      firmware-name: "t8140pmp"
-                      lts-config: "AAAAAAAAAAA5oh8AAAAAACbKDwDMKQAAxCIAAAAAEQAzswAAajwOQQEAAAA7AQAAOaIfAAAAAAAmyg8AzCkAAMQiAAAAABEAM7MAAIPgdwQCAAAADQIAABdTIQAAAAAARccPAMwpAADEIgAAAAARADOzAAAYZAtF"
+                      lts-config: "AAAAAAAAAAALJiAAAAAAAEXJDwDMKQAAxCIAAAAAEQAzswAAYpCoGwEAAAANAgAACyYgAAAAAABFyQ8AzCkAAMQiAAAAABEAM7MAAGrc2wkCAAAApAEAABmKIQAAAAAA58YPAPgqAADEIgAAAAARADOzAAAYZHEx"
-                      mc-dsid-ptd-config: "AQAAAAAAAAAQAAAAAAAAABEAAAAAAAAAEgAAAAAAAAA="
+                      mc-dsid-ptd-config: "AQAAAAAAAAAIAAAAAAAAAA8AAAAAAAAAEQAAAAAAAAA="
                       mcache-stream: [
                         ...
-                        " "
-                        " "
-                        "!"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
-                        "."
                         ...
                         ...
                         ...
-                        "2"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
-                        "B"
-                        "B"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
-                        "J"
-                        "J"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                       ]
                       ptd-range: [
                         ...
                         ...
                         ...
+                        "\""
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
+                        "NOT-USED"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
+                        "PMU-TO-CLPC"
+                        "PMU-TO-GFX"
                         ...
                         ...
                         ...
+                        "S"
                         ...
                         ...
-                        "SOC-DEV-BWR"
                         ...
                         ...
                         ...
                         ...
                         ...
                       ]
-                      region-base: 12084838400
+                      region-base: 12890144768
-                      soc-device-ps-group: 131056
+                      soc-device-ps-group: 135266176
-                      sochot-sensors: "AQAAAAIAAAADAAAABAAAAAUAAAAGAAAA"
+                      sochot-sensors: "AQAAAAIAAAADAAAABAAAAAUAAAA="
                       temp-sensor: [
                         ...
                         ...
                         ...
                         ...
-                        "Th000i"
                         ...
                         ...
-                        "k"
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
                         ...
-                        "}"
                       ]
                     }
                   }
                 ]
                 clock-gates: [
-                  "^"
-                  "_"
+                  "d"
+                  "e"
                 ]
-                interrupts: "tgIAALUCAAC4AgAAtwIAAA=="
+                interrupts: "OAMAADcDAAA6AwAAOQMAAA=="
-                iommu-parent: "^"
+                iommu-parent: "Z"
                 power-gates: [
-                  "^"
-                  "_"
+                  "d"
+                  "e"
                 ]
                 reg: [
                   {
-                    addr: 3233808384
+                    addr: 4041211904
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 3229941760
+                    addr: 4035248128
                   }
                   {
-                    addr: 3226468352
+                    addr: 4031774720
                   }
                   {
-                    addr: 3225223168
+                    addr: 4030529536
                   }
                 ]
               }
             }
             {
               aic-timebase: {
-                reg: {
-                  addr: 12097945600
-                  size: 4096
-                }
               }
             }
             {
               dart-pmp: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
-                AAPL,phandle: 93
+                AAPL,phandle: 89
                 children: [
                   {
                     mapper-pmp: {
-                      AAPL,phandle: 94
+                      AAPL,phandle: 90
                     }
                   }
                   {
                     mapper-pmp-ptd-fwd: {
-                      AAPL,phandle: 95
+                      AAPL,phandle: 91
                     }
                   }
                 ]
-                dapf-instance-0: "AMABIAIAAAAAEAUgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADABSACAAAAABAJIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAwAkgAgAAAAAQDSACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAMANIAIAAAAAEBEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAFiACAAAAAMDyIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQEAgAgAAAGBAQCACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEBgIAIAAABgQGAgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAgCACAAAAYECAIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAABDkAgAAABBQGuQCAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAwEAAADkEAIAAAAAAOYQAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAA5BECAAAAAADmEQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAgJARAwAAAP9/kREDAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEDRkAIAAAD/P+KQAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACA5xACAAAAAADvEAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAgOcRAgAAAAAA7xECAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAICDEQMAAAAI34MRAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAA=="
+                dapf-instance-0: "AAACIAIAAAAAUAUgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAABiACAAAAAFAJIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAAAogAgAAAABQDSACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAAAOIAIAAAAAUBEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAQCACAAAAcEBAIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQGAgAgAAAHBAYCACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAECAIAIAAABwQIAgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAEAgDAAAAFFAaCAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEDAQAAAOQQAgAAAP//5xACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAADkEQIAAAD//+cRAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADAlgEEAAAA/7+XAQQAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQNGABAAAAP8/4oAEAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIDnEAIAAAAAAO8QAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACA5xECAAAAAADvEQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAgIYBBAAAAAjfhgEEAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEAATwIAAACEQABPAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACAAE8CAAAAQMEATwIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQABQAgAAAIRAAFACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIAAUAIAAABAwQBQAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAAFECAAAAhEAAUQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAgABRAgAAAEDBAFECAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAMABIAIAAAAA4AEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADABSACAAAAAOAFIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAwAkgAgAAAADgCSACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAMANIAIAAAAA4A0gAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACALAgDAAAAUIAsCAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQA="
-                interrupts: 697
+                interrupts: 827
-                n-apfs-instance-0: 16
+                n-apfs-instance-0: " "
                 reg: [
                   {
-                    addr: 3224371200
+                    addr: 4029677568
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 3224387584
+                    addr: 4029743104
                   }
                 ]
               }
             }
             {
               sep: {
-                AAPL,phandle: 96
+                AAPL,phandle: 92
                 children: [
                   {
                     iop-sep-nub: {
-                      rom-panic-bytes: 456
-                      AAPL,phandle: 97
+                      AAPL,phandle: 93
                       children: [
                         {
-                          Ocelot: {
-                            AAPL,phandle: 98
-                            children: [
-                            ]
-                          }
+                          Sandcat: {
+                            AAPL,phandle: 94
+                            children: [
+                            ]
+                          }
                         }
                         {
                           xART: {
-                            AAPL,phandle: 99
+                            AAPL,phandle: 95
                           }
                         }
+                        {
+                          InvalidateHmac: {
+                            AAPL,phandle: 96
+                            children: [
+                            ]
+                            config: 1
+                            reg-block: "AMAtCAMAAAAAgAEAAAAAAA=="
+                            sio-hmac1-disable-mask: 1
+                            sio-hmac1-offset: "<"
+                          }
+                        }
                       ]
                       function-wait_for_power_gate: [
                         ...
-                        "tiaWk"
+                        "tiaWi"
                       ]
                     }
                   }
                 ]
-                interrupts: "SQEAAEgBAABLAQAASgEAAA=="
+                interrupts: "WAEAAFcBAABaAQAAWQEAAA=="
                 iommu-parent: [
-                  "e"
-                  "f"
+                  "b"
+                  "c"
                 ]
                 reg: [
                   {
-                    addr: 2453667840
+                    addr: 1918894080
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 2449801216
+                    addr: 1912930304
                   }
                 ]
               }
             }
             {
               dart-sep: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
+                exclave-sid: 2
+                vm-base-2: 2199023271936
+                vm-size-2: 4294901760
-                AAPL,phandle: 100
+                AAPL,phandle: 97
                 children: [
                   {
                     mapper-sep: {
-                      AAPL,phandle: 101
+                      AAPL,phandle: 98
                     }
                   }
                   {
                     mapper-sep-mpm: {
-                      AAPL,phandle: 102
+                      AAPL,phandle: 99
                     }
                   }
+                  {
+                    mapper-sep-exclave: {
+                      AAPL,phandle: 100
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 2
+                    }
+                  }
                 ]
-                interrupts: 334
+                interrupts: 353
                 reg: {
-                  addr: 2429288448
+                  addr: 1891106816
-                  size: 16384
+                  size: 131072
                 }
-                sid-count: 2
+                sid-count: 3
               }
             }
             {
               sio: {
-                AAPL,phandle: 103
+                AAPL,phandle: 102
                 children: [
                   {
                     iop-sio-nub: {
-                      AAPL,phandle: 104
+                      AAPL,phandle: 103
                       children: [
                         {
                           sio-dma: {
-                            AAPL,phandle: 105
+                            AAPL,phandle: 104
                           }
                         }
                       ]
                     }
                   }
                 ]
-                clock-gates: 416
+                clock-gates: 288
-                device-type: "SVBTZAQAAAAAAAAAUkFVZAYAAAAAAAAAQVBEZAUAAAAMAAAA"
+                device-type: "SVBTZAQAAAAAAAAAUkFVZAYAAAAAAAAAQVBEZAIAAAAAAAAA"
                 dmashim: [
                   ...
-                  "@"
                   ...
                   ...
                   ...
                   ...
                   ...
                 ]
-                interrupts: "gwMAAIIDAACFAwAAhAMAAA=="
+                interrupts: "ZQQAAGQEAABnBAAAZgQAAA=="
-                iommu-parent: "k"
+                iommu-parent: "j"
-                power-gates: 416
+                power-gates: 288
                 reg: [
                   {
-                    addr: 2512388096
+                    addr: 6272581632
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 2508521472
+                    addr: 6266617856
                   }
                 ]
               }
             }
             {
               dart-sio: {
-                error-reflector: 11938037760
-                AAPL,phandle: 106
+                AAPL,phandle: 105
                 children: [
                   {
                     mapper-sio: {
-                      AAPL,phandle: 107
+                      AAPL,phandle: 106
                     }
                   }
                   {
                     mapper-aes: {
-                      AAPL,phandle: 108
+                      AAPL,phandle: 107
                     }
                   }
-                  {
-                    mapper-admac: {
-                      AAPL,phandle: 109
-                      allow-subpage-mapping: null
-                      children: [
-                      ]
-                      compatible: "iommu-mapper"
-                      device_type: "dart-mapper"
-                      reg: 2
-                    }
-                  }
                 ]
-                interrupts: 892
+                interrupts: 1120
                 reg: {
-                  addr: 2499821568
+                  addr: 6258294784
-                  size: 16384
+                  size: 131072
                 }
-                sid: "AAAAAAEAAAACAAAA"
+                sid: 4294967296
               }
             }
             {
               ans: {
-                ignore-gating: null
-                nvme-prp-flush-wa: null
-                nvme-vdma-wa: null
+                msp-phy-fw-path: "t303.aus5"
+                nvme-num-sl: 2
+                nvme-secure-bar: null
+                nvme-tl-wa: null
-                AAPL,phandle: 110
+                AAPL,phandle: 108
                 children: [
                   {
                     iop-ans-nub: {
-                      AAPL,phandle: 111
+                      AAPL,phandle: 109
                     }
                   }
                 ]
-                clock-gates: null
+                clock-gates: 308
                 function-spi0_mosi_config: [
-                  "("
+                  "'"
+                  "OIPG!"
                 ]
                 function-spi0_sclk_config: [
-                  "("
+                  "'"
+                  "OIPG\""
                 ]
-                interrupts: "IwMAACIDAAAlAwAAJAMAAEoDAAA="
+                interrupts: "8AMAAO8DAADyAwAA8QMAAA8EAAA="
-                iommu-parent: "p"
+                iommu-parent: "n"
-                power-gates: null
+                power-gates: 308
                 reg: [
                   {
-                    addr: 4181721088
+                    addr: 6331301888
-                    size: 442368
+                    size: 557056
                   }
                   ...
-                  {
-                  }
-                  {
-                  }
-                  {
-                  }
                   {
-                    addr: 4245684224
+                    addr: 6403653632
-                    size: 278528
+                    size: 131072
                   }
+                  {
+                  }
+                  {
+                    addr: 6404702208
+                    size: 16384
+                  }
+                  {
+                    addr: 6404833280
+                    size: 16384
+                  }
                   {
-                    addr: 4177854464
+                    addr: 6325338112
                   }
                   ...
                   {
-                    addr: 4258004992
+                    addr: 6405488640
                   }
                   {
-                    addr: 4211081216
+                    addr: 6358564864
                   }
                   {
-                    addr: 4256759808
+                    addr: 6404243456
                   }
                   {
-                    addr: 4258561024
+                    addr: 6406044672
                   }
-                  {
-                    addr: 4258660352
-                    size: 32768
-                  }
                   {
-                    addr: 4258725888
+                    addr: 7479230464
-                    size: 32768
+                    size: 65536
                   }
                 ]
-                tunable-table-bundle: "qkiwvzhn"
+                tunable-table-bundle: "uxgixvoq"
               }
             }
             {
               sart-ans: {
+                power-canary-offset: 0
-                AAPL,phandle: 112
+                AAPL,phandle: 110
                 reg: [
                   {
-                    addr: 4257546240
+                    addr: 6405029888
                   }
-                  {
-                  }
                   {
-                    addr: 4258004992
+                    addr: 6406029312
                   }
+                  {
+                    addr: 6405488640
+                    size: 16384
+                  }
                 ]
               }
             }
             {
               smc: {
-                AAPL,phandle: 113
+                AAPL,phandle: 111
                 children: [
                   {
                     iop-smc-nub: {
-                      AAPL,phandle: 114
+                      AAPL,phandle: 112
                       children: [
                         {
                           smc-pmu: {
+                            event_name-btn4: "capture"
-                            AAPL,phandle: 115
+                            AAPL,phandle: 113
-                            event_name-btn3: "ring"
+                            event_name-btn3: "action"
                           }
                         }
                         {
                           smc-charger: {
-                            AAPL,phandle: 116
+                            AAPL,phandle: 114
                           }
                         }
                         {
                           smc-ext-charger: {
+                            hd-mic-coex: 1
-                            AAPL,phandle: 117
+                            AAPL,phandle: 115
-                            audio-driver: "AppleCS42L77Audio"
+                            audio-driver: "AppleCS42L79Audio"
                           }
                         }
                         {
                           smc-aop: {
-                            AAPL,phandle: 118
+                            AAPL,phandle: 116
                             function-link-data_enable: [
-                              "J"
+                              "="
                               ...
                             ]
                             function-link-data_param_get: [
+                              "="
                               ...
-                              "J"
                             ]
                             function-link-data_param_set: [
-                              "J"
+                              "="
                               ...
                             ]
-                            link-tx_config: "AABE7AIAAAAgAAAALQAAAAAQAAA="
+                            link-tx_config: "AABkDAMAAAAgAAAALQAAAAAQAAA="
                           }
                         }
                         {
                           smc-power-out: {
-                            AAPL,phandle: 119
+                            AAPL,phandle: 117
                           }
                         }
                         {
                           smc-charger-util: {
-                            AAPL,phandle: 120
+                            AAPL,phandle: 119
                           }
                         }
+                        {
+                          smc-acam: {
+                            AAPL,phandle: 118
+                            children: [
+                            ]
+                            compatible: "smc-acam"
+                            device_type: "smc-acam"
+                          }
+                        }
                       ]
-                      firmware-name: "t8130smc"
+                      firmware-name: "t8140smc"
-                      region-base: 12580814848
+                      region-base: 13117685760
                     }
                   }
                 ]
-                interrupts: "/wEAAP4BAAABAgAAAAIAAA=="
+                interrupts: "RgIAAEUCAABIAgAARwIAAA=="
                 reg: [
                   {
-                    addr: 3695181824
+                    addr: 4234149888
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 3691315200
+                    addr: 4228186112
                   }
                   {
-                    addr: 3699441664
+                    addr: 4236312576
-                    size: 20
+                    size: 256
                   }
                 ]
               }
             }
             {
               aon-ptd: {
-                #interrupt-cells: 1
+                #interrupt-cells: 2
-                AAPL,phandle: 121
+                AAPL,phandle: 120
-                interrupts: "AwIAAAQCAAAFAgAABgIAAAcCAAAIAgAACQIAAAoCAAALAgAADAIAAA0CAAAOAgAADwIAABACAAARAgAAEgIAABMCAAAUAgAAFQIAABYCAAAXAgAAGAIAABkCAAAaAgAAGwIAABwCAAAdAgAAHgIAAB8CAAAgAgAAIQIAACICAAA="
+                interrupts: "SgIAAEsCAABMAgAATQIAAE4CAABPAgAAUAIAAFECAABSAgAAUwIAAFQCAABVAgAAVgIAAFcCAABYAgAAWQIAAFoCAABbAgAAXAIAAF0CAABeAgAAXwIAAGACAABhAgAAYgIAAGMCAABkAgAAZQIAAGYCAABnAgAAaAIAAGkCAAA="
                 reg: [
                   {
-                    addr: 3699638272
+                    addr: 4236509184
                   }
                   {
-                    addr: 3699703808
+                    addr: 4236574720
                   }
                   {
-                    addr: 3699736576
+                    addr: 4236607488
                   }
                   {
-                    addr: 3699769344
+                    addr: 4236640256
                   }
                 ]
               }
             }
             {
               pmgrtools: {
-                AAPL,phandle: 122
+                AAPL,phandle: 121
               }
             }
             {
               pmgr: {
-                #bridges: ")"
-                apsc-snooze: 0
-                axi2af-axi-config: "ACAYEAAgGBAAIBgRACAYEAAgGBEAIBgSACAYEwAgGBAAIBgQACAYEQAgGBIAIBgQACAYEQAgGBAAIBgPACAYEAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wgA//8IAP//CAD//wg="
-                bridge-counter-configs: "AAcAAAAAAAAAAAAAAAAAAAAAAABNU1IgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABNU1IgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABNU1IgTTAgV1IAAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABNU1IgUkQAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABKUEVHIFBNU0cgRklGTwAAAAIAAQAAAABYCwYBAwwYMHj/AABKUEVHIE0wIFJEAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABKUEVHIE0wIFdSAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABKUEVHIFJEAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABBVkUgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABBVkUgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABBVkUgTTAgV1IAAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABBVkUgUkQAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABBVkQgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABBVkQgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABBVkQgTTAgV1IAAAAAAAAAAAACAQAAAw1YCwAAAAAAAAAAAABBVkQgTExUAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABBTkUgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABBTkUgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABBTkUgTTAgV1IAAAAAAAAAAAACAQAAAw1YCwAAAAAAAAAAAABBTkUgTExUAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABJU1AgUE1TRyBGSUZPAAAAAAMAAQAAAABYCwYBAwwYMHj/AABJU1AgTTAgUlQgV1IAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABJU1AgTTAgTExUIFdSAAAAAAACAQAAAQBYCwAAAAAAAAAAAABJU1AgUkQAAAAAAAAAAAAAAAcAAAACAAAAAAAAAAAAAAAAAABESVNQIFBNU0cgRklGTwAAAAIAAQAAAABYCwYBAwwYMHj/AABESVNQIEJVTEtDUFUgUkQAAAMBAQAAAABYCwYBAwwYMHj/AABESVNQIEJVTEtDUFUgV1IAAAACAQAAAwNYCwAAAAAAAAAAAABESVNQIFJUAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABHRlggUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABHRlggTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABHRlggTTAgV1IAAAAAAAAAAAACAQAAAw1YCwAAAAAAAAAAAABHRlggTExUAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABQQ0lFIFBNU0cgRklGTwAAAAIAAQAAAABYCwYBAwwYMHj/AABQQ0lFIE0wIFJEAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABQQ0lFIE0wIFdSAAAAAAAAAAACAQAAAwBYCwAAAAAAAAAAAABQQ0lFIFRPVEFMAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABBVEMwIFBNU0cgRklGTwAAAAIAAQAAAABYCwYBAwwYMHj/AABBVEMwIE0wIFJEAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABBVEMwIE0wIFdSAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABBVEMwIFJEAAAAAAAAAAAAAAcAAAACAAAAAAAAAAAAAAAAAABESVNQWCBQTVNHIEZJRk8AAAIAAQAAAABYCwYBAwwYMHj/AABESVNQWCBNMCBCVUxLIFJEAAMBAQAAAABYCwYBAwwYMHj/AABESVNQWCBNMCBMTFQgV1IAAAACAQAAAwNYCwAAAAAAAAAAAABESVNQWCBSVAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABTQlIgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABTQlIgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABTQlIgTTAgV1IAAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABTQlIgUkQAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABBTlMyIFBNU0cgRklGTwAAAAIAAQAAAABYCwYBAwwYMHj/AABBTlMyIE0wIFJEAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABBTlMyIE0wIFdSAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABBTlMyIFJEAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABQUk9SRSBQTVNHIEZJRk8AAAIAAQAAAABYCwYBAwwYMHj/AABQUk9SRSBNMCBSRAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABQUk9SRSBNMCBXUgAAAAAAAAACAQAAAw1YCwAAAAAAAAAAAABQUk9SRSBMTFQAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABTRVAgUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABTRVAgTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABTRVAgTTAgV1IAAAAAAAAAAAACAQAAAQBYCwAAAAAAAAAAAABTRVAgUkQAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAABTSU8gUE1TRyBGSUZPAAAAAAIAAQAAAABYCwYBAwwYMHj/AABTSU8gTTAgUkQAAAAAAAAAAAMBAQAAAABYCwYBAwwYMHj/AABTSU8gTTAgV1IAAAAAAAAAAAACAQAAAw1YCwAAAAAAAAAAAABTSU8gTExUAAAAAAAAAAAA"
-                bridge-counter-version: 3
-                bridge-counters: "AoAABAKABAQCgAgEAoAMBAKAEAQCgBQEAoAYBAKAHAQCgCAEAoAkBAKAKAQCgCwEAoAwBAKANAQCgDgEAoA8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
-                bridge-settings-version: 1
-                clocks: "AAADAQAAAABQTEwwX0NOVDAAAAAAAAAAAQADAgAAAABQTEwwX0NOVDEAAAAAAAAAAgADAwAAAABQTEwxX0NOVDAAAAAAAAAAAwADBAAAAABQTEwxX0NOVDEAAAAAAAAABAADBQAAAABQTEwyX0NOVDAAAAAAAAAABQADBgAAAABQTEwyX0NOVDEAAAAAAAAABgADBwAAAABQTEwzX0NOVDAAAAAAAAAABwADCAAAAABQTEwzX0NOVDEAAAAAAAAACAADCQAAAABQTEw0X0NOVDAAAAAAAAAACQADCgAAAABQTEw0X0NOVDEAAAAAAAAACgADCwAAAABQTEw1X0NOVDAAAAAAAAAACwADDAAAAABQTEw1X0NOVDEAAAAAAAAADAADDQAAAABQTEw2X0NOVDAAAAAAAAAADQADDgAAAABQTEw2X0NOVDEAAAAAAAAADgADDwAAAABQTEw3X0NOVDAAAAAAAAAADwADEAAAAABQTEw3X0NOVDEAAAAAAAAAEAADEQAAAABQTExfUENJRQAAAAAAAAAAEQADEgAAAABQTExfR0ZYAAAAAAAAAAAAEgADEwAAAABQTExfQU5FMAAAAAAAAAAAEwADFAAAAABQTExfQU5FMQAAAAAAAAAAFAADFQAAAABQTExfRENTMAAAAAAAAAAAFQADFgAAAABQTExfRENTMQAAAAAAAAAAegABFwAAAABBTkUwX0JZUAAAAAAAAAAAewABGAAAAABHRlhfQllQAAAAAAAAAAAALQEBGQAAAABGQVNUX0FGAAAAAAAAAAAALgEBGgAAAABTQlIAAAAAAAAAAAAAAAAALwEBGwAAAABQTVAAAAAAAAAAAAAAAAAAMAEBHAAAAABEUEUAAAAAAAAAAAAAAAAAMQEBHQAAAABTSU9fQQAAAAAAAAAAAAAAMgEBHgAAAABESVNQMAAAAAAAAAAAAAAAMwEBHwAAAABESVNQRVhUMAAAAAAAAAAANAEBIAAAAABBTlMAAAAAAAAAAAAAAAAANQEBIQAAAABJU1BfQwAAAAAAAAAAAAAANgEBIgAAAABNQ1UAAAAAAAAAAAAAAAAANwEBIwAAAABBTkUwX1NZUwAAAAAAAAAAOAEBJAAAAABNU1IwAAAAAAAAAAAAAAAAOQEBJQAAAABWRU5DMAAAAAAAAAAAAAAAOgEBJgAAAABJU1BSRUYwAAAAAAAAAAAAOwEBJwAAAABJU1BSRUYxAAAAAAAAAAAAAAYDKAAAAABMUFBMTF9GQVNUX0NOVDAAAQYDKQAAAABMUFBMTF9GQVNUX0NOVDEAAgYDKgAAAABMUFBMTF9WSURfQ05UMAAAAwYDKwAAAABMUFBMTF9WSURfQ05UMQAAIAcBLAAAAABBT05fU1BNSQAAAAAAAAAAIQcBLQAAAABNVFBfU0NNAAAAAAAAAAAAIgcBLgAAAABNVFAAAAAAAAAAAAAAAAAAIwcBLwAAAABBT1BfQ0xLMAAAAAAAAAAAJAcBMAAAAABBT1BfQ0xLMQAAAAAAAAAAJQcBMQAAAABBT1BfQ0xLMgAAAAAAAAAAJgcBMgAAAABBT1BfQ0xLMwAAAAAAAAAAJwcBMwAAAABBT1BfQ0xLNAAAAAAAAAAA"
-                device-bridges: "AAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEQER4fIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASEhMUFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAExYXGBkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQaGxwdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVIyQlJicoISIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
-                events: "AAABARwAHQBTT0NfVk1JTgAAAAAAAAAAAAABAh4AHwBTT0NfVk5PTQAAAAAAAAAAAAABAyAAIQBTT0NfVk1BWAAAAAAAAAAAAAABBCIAIwBTT0NfVk9WRAAAAAAAAAAAAAAABQAANgBTT0NfUEVSRl9UUkFOUwAAAAABBj8AQABEQ1NfRjEAAAAAAAAAAAAAAAABB0EAQgBEQ1NfRjIAAAAAAAAAAAAAAAABCEMARABEQ1NfRjMAAAAAAAAAAAAAAAABCUUARgBEQ1NfRjQAAAAAAAAAAAAAAAABCkcASABEQ1NfRjUAAAAAAAAAAAAAAAAACwAAVwBEQ1NfUEVSRl9UUkFOUwAAAAABDFoAWwBBVkVfVk1JTgAAAAAAAAAAAAABDVwAXQBBVkVfVk5PTQAAAAAAAAAAAAABDl4AXwBBVkVfVk1BWAAAAAAAAAAAAAAADwAAaABBVkVfUEVSRl9UUkFOUwAAAAABEGsAbABESVNQX1ZNSU5fTk9FWFQAAAABEW0AbgBESVNQX1ZNSU4AAAAAAAAAAAABEm8AcABESVNQX1ZOT01fTk9FWFQAAAABE3EAcgBESVNQX1ZOT00AAAAAAAAAAAABFHMAdABESVNQX1ZNQVhfTk9FWFQAAAABFXUAdgBESVNQX1ZNQVgAAAAAAAAAAAAAFgAAeQBESVNQX1BFUkZfVFJBTlMAAAABFwEBAAFBRl9GQVNUX0NMS19TTE8AAAAGGFsBWgFQQ1BVX0FEQ0xLX1RSSUcAAAAGGV0BXAFQQ1BVX0FEU1dUUkcAAAAAAAAGGl8BXgFQQ1BVX0FESFdUUkcAAAAAAAAGG2EBYAFQQ1BVX0RJVEhSX1RSSUcAAAAGHGMBYgFQQ1BVX0RUSFNXVFJHAAAAAAAGHWUBZAFQQ1BVX0RUSEhXVFJHAAAAAAAGHmcBZgFQQ1BVX1BQVF9UUklHAAAAAAAGH2kBaAFQQ1BVX1BQVF9TV1RSRwAAAAAGIGsBagFQQ1BVX1BQVF9IV1RSRwAAAAAGIW0BbAFQQ1BVX0VYVF9UUklHMAAAAAAGIm8BbgFQQ1BVX0VYVF9UUklHMQAAAAAGI3EBcAFQQ1BVX0VYVF9UUklHMgAAAAAGJHMBcgFQQ1BVX0VYVF9UUklHMwAAAAAGJXUBdAFFQ1BVX0FEQ0xLX1RSSUcAAAAGJncBdgFFQ1BVX0FEU1dUUkcAAAAAAAAGJ3kBeAFFQ1BVX0FESFdUUkcAAAAAAAAGKHsBegFFQ1BVX0RJVEhSX1RSSUcAAAAGKX0BfAFFQ1BVX0RUSFNXVFJHAAAAAAAGKn8BfgFFQ1BVX0RUSEhXVFJHAAAAAAAGK4EBgAFFQ1BVX1BQVF9UUklHAAAAAAAGLIMBggFFQ1BVX1BQVF9TV1RSRwAAAAAGLYUBhAFFQ1BVX1BQVF9IV1RSRwAAAAAGLocBhgFFQ1BVX0VYVF9UUklHMAAAAAAGL4kBiAFFQ1BVX0VYVF9UUklHMQAAAAAGMIsBigFFQ1BVX0VYVF9UUklHMgAAAAAGMY0BjAFFQ1BVX0VYVF9UUklHMwAAAAAGMo8BjgFDMVBUX0FEQ0xLX1RSSUcAAAAGM5EBkAFDMVBUX0FEU1dUUkcAAAAAAAAGNJMBkgFDMVBUX0FESFdUUkcAAAAAAAAGNZUBlAFDMVBUX0RJVEhSX1RSSUcAAAAGNpcBlgFDMVBUX0RUSFNXVFJHAAAAAAAGN5kBmAFDMVBUX0RUSEhXVFJHAAAAAAAGOJsBmgFDMVBUX1BQVF9UUklHAAAAAAAGOZ0BnAFDMVBUX1BQVF9TV1RSRwAAAAAGOp8BngFDMVBUX1BQVF9IV1RSRwAAAAAGO6EBoAFDMVBUX0VYVF9UUklHMAAAAAAGPKMBogFDMVBUX0VYVF9UUklHMQAAAAAGPaUBpAFDMVBUX0VYVF9UUklHMgAAAAAGPqcBpgFDMVBUX0VYVF9UUklHMwAAAAAAPwAAqAFTT0NfVFZNX1RFTVBfMAAAAAAAQAAAqQFTT0NfVFZNX1RFTVBfMQAAAAAAQQAAqgFTT0NfVFZNX1RFTVBfMgAAAAAAQgAAqwFTT0NfVFZNX1RFTVBfMwAAAAAAQwAArAFEQ1NfVFZNX1RFTVBfMAAAAAAARAAArQFEQ1NfVFZNX1RFTVBfMQAAAAAARQAArgFEQ1NfVFZNX1RFTVBfMgAAAAAARgAArwFEQ1NfVFZNX1RFTVBfMwAAAAAARwAAsAFHRlhfVFZNX1RFTVBfMAAAAAAASAAAsQFHRlhfVFZNX1RFTVBfMQAAAAAASQAAsgFHRlhfVFZNX1RFTVBfMgAAAAAASgAAswFHRlhfVFZNX1RFTVBfMwAAAAAASwAAtAFESVNQX1RWTV9URU1QXzAAAAAATAAAtQFESVNQX1RWTV9URU1QXzEAAAAATQAAtgFESVNQX1RWTV9URU1QXzIAAAAATgAAtwFESVNQX1RWTV9URU1QXzMAAAAATwAAuAFBVkVfVFZNX1RFTVBfMAAAAAAAUAAAuQFBVkVfVFZNX1RFTVBfMQAAAAAAUQAAugFBVkVfVFZNX1RFTVBfMgAAAAAAUgAAuwFBVkVfVFZNX1RFTVBfMwAAAAABU70BvAFTT0NIT1QwAAAAAAAAAAAAAAABVL8BvgFTT0NIT1QxAAAAAAAAAAAAAAAAVQAAwAFBTkVfQ05UMF9BQ0MxAAAAAAAAVgAAwQFBTkVfQ05UMV9BQ0MxAAAAAAAAVwAAwgFBTkVfQ05UMl9BQ0MxAAAAAAAAWAAAwwFTT0NfQ1NSQU1fU1RTAAAAAAAAWQAAxAFEQ1NfQ1NSQU1fU1RTAAAAAAAAWgAAxQFHUFVfQ1NSQU1fU1RTAAAAAAAAWwAAxgFESVNQX0NTUkFNX1NUUwAAAAAAXAAAxwFBVkVfQ1NSQU1fU1RTAAAAAAAGXckByAFUSFJPVFRMRV9UUklHMAAAAAAGXssBygFUSFJPVFRMRV9UUklHMQAAAAAGX80BzAFUSFJPVFRMRV9UUklHMgAAAAAGYM8BzgFUSFJPVFRMRV9UUklHMwAAAAAGYdEB0AFUSFJPVFRMRV9UUklHNAAAAAAGYtMB0gFOVUJfU1BNSTBfSVJRMAAAAAAGY9UB1AFOVUJfU1BNSTBfSVJRMQAAAAAGZNcB1gFOVUJfU1BNSTBfSVJRMgAAAAAGZdkB2AFOVUJfU1BNSTBfSVJRMwAAAAAGZtsB2gFOVUJfU1BNSTBfSVJRNAAAAAAGZ90B3AFOVUJfU1BNSTBfSVJRNQAAAAAGaN8B3gFOVUJfU1BNSTBfSVJRNgAAAAAGaeEB4AFOVUJfU1BNSTBfSVJRNwAAAAAGauMB4gFOVUJfU1BNSTFfSVJRMAAAAAAGa+UB5AFOVUJfU1BNSTFfSVJRMQAAAAAGbOcB5gFOVUJfU1BNSTFfSVJRMgAAAAAGbekB6AFOVUJfU1BNSTFfSVJRMwAAAAAGbusB6gFOVUJfU1BNSTFfSVJRNAAAAAAGb+0B7AFOVUJfU1BNSTFfSVJRNQAAAAAGcO8B7gFOVUJfU1BNSTFfSVJRNgAAAAAGcfEB8AFOVUJfU1BNSTFfSVJRNwAAAAAGcvMB8gFPUkVEX1NQTUkwX1ZXUzAAAAAGc/UB9AFPUkVEX1NQTUkwX1ZXUzEAAAAGdPcB9gFPUkVEX1NQTUkxX1ZXUzAAAAAGdfkB+AFPUkVEX1NQTUkxX1ZXUzEAAAAAdgAA+gFBQ0NFX0tBAAAAAAAAAAAAAAAAdwAA+wFBQ0NQX0tBAAAAAAAAAAAAAAAAeAAA/AFBTkVfS0EAAAAAAAAAAAAAAAAAeQAA/QFBTlNfS0EAAAAAAAAAAAAAAAAAegAA/gFBVENfS0EAAAAAAAAAAAAAAAAAewAA/wFBVkRfS0EAAAAAAAAAAAAAAAAAfAAAAAJBVkVfS0EAAAAAAAAAAAAAAAAAfQAAAQJESVNQX0tBAAAAAAAAAAAAAAAAfgAAAgJESVNQRVhUX0tBAAAAAAAAAAAAfwAAAwJJU1BfS0EAAAAAAAAAAAAAAAAAgAAABAJKUEVHX0tBAAAAAAAAAAAAAAAAgQAABQJNU1JfS0EAAAAAAAAAAAAAAAAAggAABgJQQ0lFX0tBAAAAAAAAAAAAAAAAgwAABwJQUk9SRVNfS0EAAAAAAAAAAAAAhAAACAJTQlJfS0EAAAAAAAAAAAAAAAAAhQAACQJTRVBfS0EAAAAAAAAAAAAAAAAAhgAACgJTSU9fS0EAAAAAAAAAAAAAAAAAhwAACwJTV19BR0VOVDBfS0EAAAAAAAAAiAAADAJTV19BR0VOVDFfS0EAAAAAAAAAiQAADQJTV19BR0VOVDJfS0EAAAAAAAABig8CDgJDUEdfVEdUX0FNQ0NfS0EAAAABixECEAJUR1RfUFNfQU1DQ19LQQAAAAAAjAAAEgJDUEdfQU1DQ19LQQAAAAAAAAABjRQCEwJDUEdfVEdUX0RDU19LQQAAAAABjhYCFQJUR1RfUFNfRENTX0tBAAAAAAAAjwAAFwJDUEdfRENTX0tBAAAAAAAAAAABkBkCGAJDUEdfVEdUX1NNWDBfS0EAAAABkRsCGgJUR1RfUFNfU01YMF9LQQAAAAAAkgAAHAJDUEdfU01YMF9LQQAAAAAAAAABkx4CHQJDUEdfVEdUX0xNWDBfS0EAAAABlCACHwJUR1RfUFNfTE1YMF9LQQAAAAAAlQAAIQJDUEdfTE1YMF9LQQAAAAAAAAABliMCIgJDUEdfVEdUX0xNWDFfS0EAAAABlyUCJAJUR1RfUFNfTE1YMV9LQQAAAAAAmAAAJgJDUEdfTE1YMV9LQQAAAAAAAAABmSgCJwJDUEdfVEdUX0xNWDJfS0EAAAABmioCKQJUR1RfUFNfTE1YMl9LQQAAAAAAmwAAKwJDUEdfTE1YMl9LQQAAAAAAAAAGnAEDAANHUFVfQURDTEtfVFJJRwAAAAAGnQMDAgNHUFVfQURTV1RSRwAAAAAAAAAGngUDBANHUFVfQURIV1RSRwAAAAAAAAAGnwcDBgNHUFVfRElUSFJfVFJJRwAAAAAGoAkDCANHUFVfRFRIU1dUUkcAAAAAAAAGoQsDCgNHUFVfRFRISFdUUkcAAAAAAAAGog0DDANHUFVfUFBUX1RSSUcAAAAAAAAGow8DDgNHUFVfUFBUX1NXVFJHAAAAAAAGpBEDEANHUFVfUFBUX0hXVFJHAAAAAAAGpRMDEgNHUFVfRVhUX1RSSUcwAAAAAAAGphUDFANHUFVfRVhUX1RSSUcxAAAAAAAGpxcDFgNHUFVfRVhUX1RSSUcyAAAAAAAGqBkDGANHUFVfRVhUX1RSSUczAAAAAAAGqQEEAARBTkVfQURDTEtfVFJJRwAAAAAGqgMEAgRBTkVfQURTV1RSRwAAAAAAAAAGqwUEBARBTkVfQURIV1RSRwAAAAAAAAAGrAcEBgRBTkVfRElUSFJfVFJJRwAAAAAGrQkECARBTkVfRFRIU1dUUkcAAAAAAAAGrgsECgRBTkVfRFRISFdUUkcAAAAAAAAGrw0EDARBTkVfUFBUX1RSSUcAAAAAAAAGsA8EDgRBTkVfUFBUX1NXVFJHAAAAAAAGsREEEARBTkVfUFBUX0hXVFJHAAAAAAAGshMEEgRBTkVfRVhUX1RSSUcwAAAAAAAGsxUEFARBTkVfRVhUX1RSSUcxAAAAAAAGtBcEFgRBTkVfRVhUX1RSSUcyAAAAAAAGtRkEGARBTkVfRVhUX1RSSUczAAAAAAAGtgEFAAVTT0NfQURDTEtfVFJJRwAAAAAGtwMFAgVTT0NfQURTV1RSRwAAAAAAAAAGuAUFBAVTT0NfQURIV1RSRwAAAAAAAAAGuQcFBgVTT0NfRElUSFJfVFJJRwAAAAAGugkFCAVTT0NfRFRIU1dUUkcAAAAAAAAGuwsFCgVTT0NfRFRISFdUUkcAAAAAAAAGvA0FDAVTT0NfUFBUX1RSSUcAAAAAAAAGvQ8FDgVTT0NfUFBUX1NXVFJHAAAAAAAGvhEFEAVTT0NfUFBUX0hXVFJHAAAAAAAGvxMFEgVTT0NfRVhUX1RSSUcwAAAAAAAGwBUFFAVTT0NfRVhUX1RSSUcxAAAAAAAGwRcFFgVTT0NfRVhUX1RSSUcyAAAAAAAGwhkFGAVTT0NfRVhUX1RSSUczAAAAAAABwzIHMQdTTFBfTUVESUEAAAAAAAAAAAABxDQHMwdTTFBfRERSAAAAAAAAAAAAAAABxTYHNQdBV0FLRQAAAAAAAAAAAAAAAAABxjgHNwdTTFBfUzJSAAAAAAAAAAAAAAABxzoHOQdERUVQX1dBSVQAAAAAAAAAAAACyAAAAABFQ1BVX0RQRV9USFJUTAAAAAACyQAADABFQ1BVMAAAAAAAAAAAAAAAAAACygAAEABFQ1BVMQAAAAAAAAAAAAAAAAACywAAFABFQ1BVMgAAAAAAAAAAAAAAAAACzAAAGABFQ1BVMwAAAAAAAAAAAAAAAAAHzQAAAABQQ1BVX0RQRV9USFJUTAAAAAAHzgAADABQQ1BVMAAAAAAAAAAAAAAAAAAHzwAAEABQQ1BVMQAAAAAAAAAAAAAAAAEA0gAAJwFTMlJfV0tfVElNRQAAAAAAAAEA0wAAKQFERFJfV0tfVElNRQAAAAAAAAEA1AAAJgFNRURJQV9XS19USU1FAAAA"
-                first-acc-dvfm-map-state: 1
-                int-dis-threshold: 12000
-                optional-bridge-mask: 0
-                perf-regs: [
-                  "|"
-                  "5"
-                  ";"
-                ]
-                power-domains: "ADwBAQAAAABBTUNDMAAAAAAAAAAAAAAAAD0BAgAAAABEQ1MwAAAAAAAAAAAAAAAAAD4BAwAAAABEQ1MyAAAAAAAAAAAAAAAAAD8BBAAAAABEQ1MxAAAAAAAAAAAAAAAAAEABBQAAAABEQ1MzAAAAAAAAAAAAAAAAAEEBBgAAAABTTVgwAAAAAAAAAAAAAAAAAEIBBwAAAABMTVgwAAAAAAAAAAAAAAAAAEMBCAAAAABMTVgxAAAAAAAAAAAAAAAAAEQBCQAAAABMTVgyAAAAAAAAAAAAAAAABEUBCgECEQBESVNQX0NQVQAAAAAAAAAAAEYBCwAAAABESVNQX0dQMAAAAAAAAAAAAEcBDAAAAABESVNQX0dQMQAAAAAAAAAAAEgBDQAAAABESVNQX0NNQgAAAAAAAAAAAEkBDgAAAABESVNQX1BQUAAAAAAAAAAAAEoBDwAAAABESVNQX0hJTE8AAAAAAAAAAEsBEAAAAABESVNQX0lUTAAAAAAAAAAABEwBEQECGwBESVNQRVhUX0NQVQAAAAAAAE0BEgAAAABESVNQRVhUX0dQMAAAAAAAAE4BEwAAAABESVNQRVhUX0dQMQAAAAAAAE8BFAAAAABESVNQRVhUX1BQUAAAAAAAAFABFQAAAABQTVAAAAAAAAAAAAAAAAAAAFEBFgAAAABQTVNfU1JBTQAAAAAAAAAAAFIBFwAAAABBUENJRV9TWVMAAAAAAAAAAFMBGAAAAABHRlgAAAAAAAAAAAAAAAAAAFQBGQAAAABTRVAAAAAAAAAAAAAAAAAAAFUBGgAAAABJU1BDUFUwAAAAAAAAAAAAAFYBGwAAAABJU1BDUFUxAAAAAAAAAAAAAFcBHAAAAABBTlMAAAAAAAAAAAAAAAAABFgBHQEAHgFBTkVfU1lTAAAAAAAAAAAAAFkBHgAAAABBTkVfQ1BVAAAAAAAAAAAAACgHHwAAAABOVUJfRkFCAAAAAAAAAAAAACkHIAAAAABOVUJfU1JBTQAAAAAAAAAAACoHIQAAAABEQkdfU1dUQ0gAAAAAAAAAACsHIgAAAABBT1BfQ1BVAAAAAAAAAAAAACwHIwAAAABBT1BfRkxUUgAAAAAAAAAAAC0HJAAAAABTTUNfQ1BVAAAAAAAAAAAAAC4HJQAAAABTTUNfRkFCAAAAAAAAAAAAAC8HJgAAAABNVFBfRkFCAAAAAAAAAAAAADAHJwAAAABNVFBfQ1BVAAAAAAAAAAAA"
-                ps-regs: [
-                  {
-                    reg: 1
-                    unk: 2095105
-                  }
-                  {
-                    reg: 1
-                    off: 16384
-                  }
-                  {
-                    reg: 1
-                    off: 16640
-                  }
-                  {
-                    reg: 1
-                    off: 32768
-                    unk: 224
-                  }
-                  {
-                    reg: 1
-                    off: 49152
-                  }
-                  {
-                    reg: 1
-                    off: 65536
-                  }
-                  {
-                    reg: 1
-                    off: 81920
-                  }
-                  {
-                    unk: 831
-                  }
-                  {
-                    off: 256
-                    unk: 4294967295
-                  }
-                  {
-                    off: 512
-                    unk: 4294967295
-                  }
-                  {
-                    off: 768
-                    unk: 52428791
-                  }
-                  {
-                    off: 3072
-                    unk: 1
-                  }
-                  {
-                    off: 16384
-                    unk: 8191
-                  }
-                  {
-                    off: 32768
-                    unk: 31
-                  }
-                  {
-                    off: 49152
-                  }
-                  {
-                    off: 65536
-                    unk: 1
-                  }
-                ]
-                pwrgate-regs: "AAAAAAxAAgD/////AAAAgAAAAAAMUAIA/////wAAAIAAAAAADGACAP+/AAAAAACA"
-                skip-ps-lock: 1
+                acc-harvesting: 1
+                ap-voter-agent-idx: 3
+                axi2af-hack: 1023
+                boost-agent: "AAAAAToAAABESVNQX0lOVF9EQ1AAAAAAAAABAlABAABESVNQX0lOVF9NMwAAAAAAAAACAzsAAABESVNQX0VYVDBfRENQAAAAAAADBFEBAABESVNQX0VYVDBfTTMAAAAAAAAEBTkAAABBTlMAAAAAAAAAAAAAAAAAAAAFBiEBAABVU0JfQVVEAAAAAAAAAAAA"
+                bwr-agent: [
+                  "DISP_INT"
+                  "ISP"
+                  "DISP_EXT0"
+                  "SPARE0"
+                  "SPARE1"
+                ]
+                clpc-voter-agent-idx: 1
+                cluster-agent: [
+                  "AVE"
+                ]
+                dvmr-agent: "AAAAAToAAABESVNQX0lOVAAAAAAAAAAAAAABAjsAAABESVNQX0VYVDAAAAAAAAAA"
+                edt-property-ver: 2
+                perf-counters: [
+                  "SBR"
+                  "PMS_BUSIF"
+                  "PMS"
+                  "PMC"
+                  "ISPSENS0"
+                  "ISPSENS1"
+                  "APCIE_PHY_SW"
+                  "SIO"
+                  "SIO_CPU"
+                  "AFIMCCNI0"
+                  "PIOGW"
+                  "AFGGFXNI0"
+                  "AFCMCCNI0"
+                  "AMCC0_P0"
+                  "AMCC0_P1"
+                  "AMCC0_P2"
+                  "AMCC0_P3"
+                  "DCS0"
+                  "DCS2"
+                  "DCS1"
+                  "DCS3"
+                  "AFINS0"
+                  "AFISOCNI0"
+                  "AFISOCNI1"
+                  "AFISOCNI2"
+                  "DISP_CPU"
+                  "DISP_GP0"
+                  "DISP_GP1"
+                  "DISP_CMB"
+                  "DISP_PPP"
+                  "DISP_HILO"
+                  " "
+                  "DISPEXT0_CPU"
+                  "!"
+                  "DISPEXT0_GPPP"
+                  "\""
+                  "JPG"
+                  "#"
+                  "MSR"
+                  "$"
+                  "MSR_ASE_CORE"
+                  "%"
+                  "PMP"
+                  "&"
+                  "PMS_SRAM"
+                  "'"
+                  "APCIE_SYS_GP"
+                  "("
+                  "APCIE_SYS_ST"
+                  ")"
+                  "GFX"
+                  "*"
+                  "SEP"
+                  "+"
+                  "ISP_CPU_CORE0"
+                  ","
+                  "ISP_CPU_CORE1"
+                  "-"
+                  "VENC0_SYS"
+                  "."
+                  "VENC1_SYS"
+                  "/"
+                  "AVD_SYS"
+                  "0"
+                  "ANS"
+                  "1"
+                  "ANE_CPU"
+                  "2"
+                  "DEBUG_GATED"
+                  "3"
+                  "NUB_SPMI0"
+                  "4"
+                  "NUB_SPMI1"
+                  "5"
+                  "NUB_SPMI_A0"
+                  "6"
+                  "NUB_AON"
+                  "7"
+                  "SMC_AON"
+                  "8"
+                  "SMC_PTD"
+                  "9"
+                  "NUB_HE_NRCS0"
+                  ":"
+                  "NUB_HE_NRCS1"
+                  ";"
+                  "NUB_FABRIC"
+                  "<"
+                  "NUB_SRAM"
+                  "="
+                  "DEBUG_SWITCH"
+                  ">"
+                  "AOP_BASE"
+                  "?"
+                  "AOP_SRAM"
+                  "@"
+                  "AOP_SCM"
+                  "A"
+                  "AOP_SPI0"
+                  "B"
+                  "AOP_SPI1"
+                  "C"
+                  "AOP_SPMI0"
+                  "D"
+                  "AOP_SPMI1"
+                  "E"
+                  "AOP_HE_NRCS0"
+                  "F"
+                  "AOP_HE_NRCS1"
+                  "G"
+                  "AOP_CPU"
+                  "H"
+                  "AOP2_CPU"
+                  "I"
+                  "AOP_FILTER"
+                  "J"
+                  "SMC_CPU"
+                  "K"
+                  "SMC_FABRIC"
+                  "L"
+                  "MTP_FABRIC"
+                  "M"
+                  "MTP_BASE"
+                  "N"
+                  "MTP_SCM_FABRIC"
+                  "O"
+                  "MTP_SPI0"
+                  "P"
+                  "MTP_SRAM"
+                  "Q"
+                  "MTP_CPU"
+                  "R"
+                  "AUDIO_A"
+                  "S"
+                  "AUDIO_BASE_S_ADMA_A"
+                  "T"
+                  "AUDIO_BASE_NS_ADMA_A"
+                  "U"
+                  "AUDIO_LEAP_A"
+                  "V"
+                  "AUDIO_LEAP_S_ADMA_A"
+                  "W"
+                  "AUDIO_LEAP_NS_ADMA_A"
+                  "PLL0_CNT0"
+                  "PLL0_CNT1"
+                  "PLL1_CNT0"
+                  "PLL1_CNT1"
+                  "PLL2_CNT0"
+                  "PLL2_CNT1"
+                  "PLL3_CNT0"
+                  "PLL3_CNT1"
+                  "PLL4_CNT0"
+                  "PLL4_CNT1"
+                  "PLL5_CNT0"
+                  "PLL5_CNT1"
+                  "PLL6_CNT0"
+                  "PLL6_CNT1"
+                  "PLL_PCIE"
+                  "PLL_ANE0"
+                  "PLL_ANE1"
+                  "PLL_DCSCLKGEN0"
+                  "PLL_DCSCLKGEN1"
+                  "k"
+                  "ANE0_BYP"
+                  "l"
+                  "GFX_BYP"
+                  "m"
+                  "FAST_AF"
+                  "n"
+                  "SBR"
+                  "o"
+                  "PMP"
+                  "p"
+                  "SIO_A"
+                  "q"
+                  "AMC_UFDI_DATA"
+                  "r"
+                  "MCU"
+                  "s"
+                  "DISP0"
+                  "t"
+                  "DISPEXT0"
+                  "u"
+                  "MSR0"
+                  "v"
+                  "ANS"
+                  "w"
+                  "ISP_C"
+                  "x"
+                  "VENC0"
+                  "y"
+                  "VENC1"
+                  "z"
+                  "ANE0_SYS"
+                  "LPPLL_FAST_CNT0"
+                  "LPPLL_FAST_CNT1"
+                  "LPPLL_VID_CNT0"
+                  "LPPLL_VID_CNT1"
+                  "LPPLL_AOP2_CNT0"
+                  "LPPLL_AOP2_CNT1"
+                  "AON_SPMI_REF"
+                  "MTP_SCM"
+                  "MTP"
+                  "AUDIO"
+                  "AOP_CLK_SEL_0"
+                  "AOP_CLK_SEL_1"
+                  "AOP_CLK_SEL_2"
+                  "AOP_CLK_SEL_3"
+                  "AOP_CLK_SEL_4"
+                  "FAB_MC0"
+                  "FAB_GFX0"
+                  "FAB_AFC0"
+                  "AMCC0_P0"
+                  "AMCC0_P1"
+                  "AMCC0_P2"
+                  "AMCC0_P3"
+                  "DCS0"
+                  "DCS2"
+                  "DCS1"
+                  "DCS3"
+                  "FAB_SW0"
+                  "FAB_AG0"
+                  "FAB_AG1"
+                  "FAB_AG2"
+                  "DISP_CPU"
+                  "DISP_GP0"
+                  "DISP_GP1"
+                  "DISP_CMB"
+                  "DISP_PPP"
+                  "DISP_HILO"
+                  "DISPEXT0_CPU"
+                  "DISPEXT0_GPPP"
+                  "MSR"
+                  "MSR_ASE"
+                  "PMP"
+                  "PMS_SRAM"
+                  "APCIE_SYS_GP"
+                  "APCIE_SYS_ST"
+                  "GFX"
+                  "SEP"
+                  "ISP_CPU_CORE0"
+                  "ISP_CPU_CORE1"
+                  "ANS"
+                  "ANE_CPU"
+                  "NUB_FABRIC"
+                  "NUB_SRAM"
+                  "DEBUG_SWITCH"
+                  "AOP_CPU"
+                  "AOP2_CPU"
+                  "AOP_FILTER"
+                  "SMC_CPU"
+                  "SMC_FABRIC"
+                  "MTP_FABRIC"
+                  "MTP_CPU"
+                  "SOC_PERFSTAT_00"
+                  "SOC_PERFSTAT_01"
+                  "SOC_VPROXY"
+                  "SOC_VMIN"
+                  "SOC_VNOM"
+                  "SOC_VMAX"
+                  "SOC_VOVD"
+                  "SOC_PERFSTAT_07"
+                  "SOC_PERFSTAT_08"
+                  "SOC_PERFSTAT_09"
+                  "SOC_PERFSTAT_10"
+                  "SOC_PERFSTAT_11"
+                  "SOC_PERFSTAT_12"
+                  "SOC_PERFSTAT_13"
+                  "SOC_PERFSTAT_14"
+                  "SOC_PERFSTAT_15"
+                  "SOC_PERFSTAT_TRANS_TIME"
+                  "DCS_PERFSTAT_00"
+                  "DCS_FAST_RECONFIG"
+                  "DCS_AOP_DDR"
+                  "DCS_COLD_BOOT"
+                  "DCS_F1"
+                  "DCS_F2"
+                  "DCS_F3"
+                  "DCS_F4"
+                  "DCS_F5"
+                  "DCS_PERFSTAT_09"
+                  "DCS_PERFSTAT_10"
+                  "DCS_PERFSTAT_11"
+                  "DCS_PERFSTAT_12"
+                  "DCS_PERFSTAT_13"
+                  "DCS_PERFSTAT_14"
+                  "DCS_PERFSTAT_15"
+                  "DCS_PERFSTAT_TRANS_TIME"
+                  "AVE_PERFSTAT_00"
+                  "AVE_VMIN"
+                  "AVE_VNOM"
+                  "AVE_VMAX"
+                  "AVE_PERFSTAT_04"
+                  "AVE_PERFSTAT_05"
+                  "AVE_PERFSTAT_06"
+                  "AVE_PERFSTAT_07"
+                  "AVE_PERFSTAT_TRANS_TIME"
+                  "DISP_PERFSTAT_00"
+                  "DISP_PERFSTAT_01"
+                  "DISP_PERFSTAT_02"
+                  "DISP_VMIN_NO_EXT"
+                  "DISP_VMIN"
+                  "DISP_VNOM_NO_EXT"
+                  "DISP_VNOM"
+                  "DISP_VMAX_NO_EXT"
+                  "DISP_VMAX"
+                  "DISP_PERFSTAT_09"
+                  "DISP_PERFSTAT_10"
+                  "DISP_PERFSTAT_11"
+                  "DISP_PERFSTAT_12"
+                  "DISP_PERFSTAT_13"
+                  "DISP_PERFSTAT_14"
+                  "DISP_PERFSTAT_15"
+                  "DISP_PERFSTAT_TRANS_TIME"
+                  "PCPU_THROTTLE_ADCLK_TRIG"
+                  "PCPU_THROTTLE_ADCLK_SW_TRIG"
+                  "PCPU_THROTTLE_ADCLK_HW_TRIG"
+                  "PCPU_THROTTLE_DITHER_TRIG"
+                  "PCPU_THROTTLE_DITHER_SW_TRIG"
+                  "PCPU_THROTTLE_DITHER_HW_TRIG"
+                  "PCPU_THROTTLE_PPT_TRIG"
+                  "PCPU_THROTTLE_PPT_SW_TRIG"
+                  "PCPU_THROTTLE_PPT_HW_TRIG"
+                  "PCPU_THROTTLE_EXT_TRIG0"
+                  "PCPU_THROTTLE_EXT_TRIG1"
+                  "PCPU_THROTTLE_EXT_TRIG2"
+                  "PCPU_THROTTLE_EXT_TRIG3"
+                  "ECPU_THROTTLE_ADCLK_TRIG"
+                  "ECPU_THROTTLE_ADCLK_SW_TRIG"
+                  "ECPU_THROTTLE_ADCLK_HW_TRIG"
+                  "ECPU_THROTTLE_DITHER_TRIG"
+                  "ECPU_THROTTLE_DITHER_SW_TRIG"
+                  "ECPU_THROTTLE_DITHER_HW_TRIG"
+                  "ECPU_THROTTLE_PPT_TRIG"
+                  "ECPU_THROTTLE_PPT_SW_TRIG"
+                  "ECPU_THROTTLE_PPT_HW_TRIG"
+                  "ECPU_THROTTLE_EXT_TRIG0"
+                  "ECPU_THROTTLE_EXT_TRIG1"
+                  "ECPU_THROTTLE_EXT_TRIG2"
+                  "ECPU_THROTTLE_EXT_TRIG3"
+                  "C1PPT_THROTTLE_ADCLK_TRIG"
+                  "C1PPT_THROTTLE_ADCLK_SW_TRIG"
+                  "C1PPT_THROTTLE_ADCLK_HW_TRIG"
+                  "C1PPT_THROTTLE_DITHER_TRIG"
+                  "C1PPT_THROTTLE_DITHER_SW_TRIG"
+                  "C1PPT_THROTTLE_DITHER_HW_TRIG"
+                  "C1PPT_THROTTLE_PPT_TRIG"
+                  "C1PPT_THROTTLE_PPT_SW_TRIG"
+                  "C1PPT_THROTTLE_PPT_HW_TRIG"
+                  "C1PPT_THROTTLE_EXT_TRIG0"
+                  "C1PPT_THROTTLE_EXT_TRIG1"
+                  "C1PPT_THROTTLE_EXT_TRIG2"
+                  "C1PPT_THROTTLE_EXT_TRIG3"
+                  "AVE_THROTTLE_ADCLK_TRIG"
+                  "AVE_THROTTLE_ADCLK_SW_TRIG"
+                  "AVE_THROTTLE_ADCLK_HW_TRIG"
+                  "AVE_THROTTLE_DITHER_TRIG"
+                  "AVE_THROTTLE_DITHER_SW_TRIG"
+                  "AVE_THROTTLE_DITHER_HW_TRIG"
+                  "AVE_THROTTLE_PPT_TRIG"
+                  "AVE_THROTTLE_PPT_SW_TRIG"
+                  "AVE_THROTTLE_PPT_HW_TRIG"
+                  "AVE_THROTTLE_EXT_TRIG0"
+                  "AVE_THROTTLE_EXT_TRIG1"
+                  "AVE_THROTTLE_EXT_TRIG2"
+                  "AVE_THROTTLE_EXT_TRIG3"
+                  "SOC_TVM_PERFCNT_TEMP_REGION0"
+                  "SOC_TVM_PERFCNT_TEMP_REGION1"
+                  "SOC_TVM_PERFCNT_TEMP_REGION2"
+                  "SOC_TVM_PERFCNT_TEMP_REGION3"
+                  "AVE_TVM_PERFCNT_TEMP_REGION0"
+                  "AVE_TVM_PERFCNT_TEMP_REGION1"
+                  "AVE_TVM_PERFCNT_TEMP_REGION2"
+                  "AVE_TVM_PERFCNT_TEMP_REGION3"
+                  "DCS_TVM_PERFCNT_TEMP_REGION0"
+                  "DCS_TVM_PERFCNT_TEMP_REGION1"
+                  "DCS_TVM_PERFCNT_TEMP_REGION2"
+                  "DCS_TVM_PERFCNT_TEMP_REGION3"
+                  "GFX_TVM_PERFCNT_TEMP_REGION0"
+                  "GFX_TVM_PERFCNT_TEMP_REGION1"
+                  "GFX_TVM_PERFCNT_TEMP_REGION2"
+                  "GFX_TVM_PERFCNT_TEMP_REGION3"
+                  "DISP_TVM_PERFCNT_TEMP_REGION0"
+                  "DISP_TVM_PERFCNT_TEMP_REGION1"
+                  "DISP_TVM_PERFCNT_TEMP_REGION2"
+                  "DISP_TVM_PERFCNT_TEMP_REGION3"
+                  "VDD_SOC_COMM_SRAM_STATUS"
+                  "VDD_AVE_COMM_SRAM_STATUS"
+                  "VDD_DCS_COMM_SRAM_STATUS"
+                  "VDD_GPU_COMM_SRAM_STATUS"
+                  "VDD_DISP_COMM_SRAM_STATUS"
+                  "THROTTLE_TRIGGER_0"
+                  "THROTTLE_TRIGGER_1"
+                  "THROTTLE_TRIGGER_2"
+                  "THROTTLE_TRIGGER_3"
+                  "THROTTLE_TRIGGER_4"
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED0"
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED1"
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED2"
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED3"
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED4"
+                  " "
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED5"
+                  "  "
+                  "@ "
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED6"
+                  "` "
+                  "NUB_SPMI0_THROTTLE_IRQ_SELECTED7"
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED0"
+                  "!"
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED1"
+                  " !"
+                  "@!"
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED2"
+                  "`!"
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED3"
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED4"
+                  "\""
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED5"
+                  " \""
+                  "@\""
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED6"
+                  "`\""
+                  "NUB_SPMI1_THROTTLE_IRQ_SELECTED7"
+                  "ORED_SPMI0_THROTTLE_VWS0"
+                  "#"
+                  "ORED_SPMI0_THROTTLE_VWS1"
+                  " #"
+                  "@#"
+                  "ORED_SPMI1_THROTTLE_VWS0"
+                  "`#"
+                  "ORED_SPMI1_THROTTLE_VWS1"
+                  "CLLT_PERF_COUNTER_0"
+                  "CLLT_PERF_COUNTER_1"
+                  "CLLT_PERF_COUNTER_2"
+                  "$"
+                  "CLLT_PERF_COUNTER_3"
+                  " $"
+                  "CLLT_PERF_COUNTER_4"
+                  "@$"
+                  "CLLT_PERF_COUNTER_5"
+                  "`$"
+                  "CLLT_PERF_COUNTER_6"
+                  "CLLT_PERF_COUNTER_7"
+                  "CLLT_PERF_COUNTER_8"
+                  "."
+                  "FAST_AF_CLK_SLOWDOWN_VMIN"
+                  " ."
+                  "@."
+                  "SOCHOT0_L"
+                  "`."
+                  "SOCHOT1_L"
+                  "ANE_COUNT_0_ACC1_ON"
+                  "ANE_COUNT_1_ACC1_ON"
+                  "ANE_COUNT_2_ACC1_ON"
+                  "GPU_THROTTLE_ADCLK_TRIG"
+                  "GPU_THROTTLE_ADCLK_SW_TRIG"
+                  "GPU_THROTTLE_ADCLK_HW_TRIG"
+                  "GPU_THROTTLE_DITHER_TRIG"
+                  "GPU_THROTTLE_DITHER_SW_TRIG"
+                  "GPU_THROTTLE_DITHER_HW_TRIG"
+                  "GPU_THROTTLE_PPT_TRIG"
+                  "GPU_THROTTLE_PPT_SW_TRIG"
+                  "GPU_THROTTLE_PPT_HW_TRIG"
+                  "GPU_THROTTLE_EXT_TRIG0"
+                  "GPU_THROTTLE_EXT_TRIG1"
+                  "GPU_THROTTLE_EXT_TRIG2"
+                  "GPU_THROTTLE_EXT_TRIG3"
+                  "ANE_THROTTLE_ADCLK_TRIG"
+                  "ANE_THROTTLE_ADCLK_SW_TRIG"
+                  "ANE_THROTTLE_ADCLK_HW_TRIG"
+                  "ANE_THROTTLE_DITHER_TRIG"
+                  "ANE_THROTTLE_DITHER_SW_TRIG"
+                  "ANE_THROTTLE_DITHER_HW_TRIG"
+                  "ANE_THROTTLE_PPT_TRIG"
+                  "ANE_THROTTLE_PPT_SW_TRIG"
+                  "ANE_THROTTLE_PPT_HW_TRIG"
+                  "ANE_THROTTLE_EXT_TRIG0"
+                  "ANE_THROTTLE_EXT_TRIG1"
+                  "ANE_THROTTLE_EXT_TRIG2"
+                  "ANE_THROTTLE_EXT_TRIG3"
+                  "SOC_THROTTLE_ADCLK_TRIG"
+                  "SOC_THROTTLE_ADCLK_SW_TRIG"
+                  "SOC_THROTTLE_ADCLK_HW_TRIG"
+                  "SOC_THROTTLE_DITHER_TRIG"
+                  "SOC_THROTTLE_DITHER_SW_TRIG"
+                  "SOC_THROTTLE_DITHER_HW_TRIG"
+                  "SOC_THROTTLE_PPT_TRIG"
+                  "SOC_THROTTLE_PPT_SW_TRIG"
+                  "SOC_THROTTLE_PPT_HW_TRIG"
+                  "SOC_THROTTLE_EXT_TRIG0"
+                  "SOC_THROTTLE_EXT_TRIG1"
+                  "SOC_THROTTLE_EXT_TRIG2"
+                  "SOC_THROTTLE_EXT_TRIG3"
+                  "SLP_MEDIA_STATE"
+                  "SLP_DDR_STATE"
+                  "SLP_CACHE_STATE"
+                  "AWAKE_STATE"
+                  "S2R_AOP_STATE"
+                  "DEEP_WAIT_STATE"
+                  "("
+                  "ECPU_DPE_THRTL"
+                  ","
+                  "ECPU_0"
+                  "0"
+                  "ECPU_1"
+                  "4"
+                  "ECPU_2"
+                  "8"
+                  "ECPU_3"
+                  "("
+                  "PCPU_DPE_THRTL"
+                  "PCPU_0"
+                  "PCPU_1"
+                ]
+                perf-groups: "AgAAAADYBgABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAACABwABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAADABwABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAACgABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAACgABAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAwAAAAC4BwACAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAQAAAABAAwACAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAAAQAAAABAAwACAAAAEAAAAAMAAAAEAAAAAAAAAAAAAAAAAAAA"
+                pmc: 1
+                pmc-ltr-ka: 1
+                pmc-pmgr: "?"
+                pmp-voter-agent-idx: 0
+                ps-groups: "AAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAA"
+                soc-cluster-power-gating: 8
+                soc-clusters: "AAAAAQAAAAAAAAAARUFDQwAAAAAAAAAAAAAAAAEAAAIAAAAAAAAAAFBBQ0MAAAAAAAAAAAAAAAACAgUDZAAAAAAAAAtBVkUAAAAAAAAAAAAAAAAAAwAABAAAAAAAAAAARElTUAAAAAAAAAAAAAAAAAQAAAUAAAAAAAAAAERDUwAAAAAAAAAAAAAAAAA="
+                voter-agent: [
+                  "PMP"
+                  "CLPC"
+                  "GFX"
+                  "AP"
+                ]
+                voter-rail-data: "AAABAAEAAABEQ1MAAAAAAAAAAAAAAAAAAQACAAIAAABTT0MAAAAAAAAAAAAAAAAAAgAEAAMAAABESVNQAAAAAAAAAAAAAAAAAwAIAAQAAABBVkUAAAAAAAAAAAAAAAAA"
-                ap-wake-sources: [
-                  "3"
-                  "AOP.OutboxNotEmpty"
-                  "AOP.CPUWakeupAP"
-                  "NUB.WakeupAP"
-                  "NUB.GPIO.IRQ6"
-                  "t"
-                  "NUB.APWatchdog"
-                  "s"
-                  "NUB.APWakeupTime"
-                  "NUB.SPMI0.SW3"
-                  "E"
-                  "AOP.SPMI0.SW3"
-                  "I"
-                  "AOP.SPMI1.SW3"
-                  "NUB.SPMI1.SW3"
-                  "SMC.CPUWakeupAP"
-                  "SMC.OutboxNotEmpty"
-                  "W"
-                  "MTP.DOCK.CHANNELS.AP0.IRQ"
-                  "M"
-                  "ATC0_PMGR_USB_WAKEUP"
-                ]
+                ap-wake-sources: "AAAAAEFPUC5BSUNXYWtldXBBUAAAAAAAAAAAAAAAAAAAAAAABQAAAEFPUC5DUFVXYWtldXBBUAAAAAAAAAAAAAAAAAAAAAAAKgAAAEFPUC5PdXRib3hOb3RFbXB0eQAAAAAAAAAAAAAAAAAAPgAAAEFPUC5TUE1JMC5TVzMAAAAAAAAAAAAAAAAAAAAAAAAAQgAAAEFPUC5TUE1JMS5TVzMAAAAAAAAAAAAAAAAAAAAAAAAARgAAAEFUQzBfUE1HUl9VU0JfV0FLRVVQAAAAAAAAAAAAAAAAUAAAAE1UUC5ET0NLLkNIQU5ORUxTLkFQMC5JUlEAAAAAAAAAYwAAAE1UUC5PVVRCT1guTi5FTVBUWV9JUlEAAAAAAAAAAAAAbQAAAE5VQi5BUFdha2V1cFRpbWUAAAAAAAAAAAAAAAAAAAAAbgAAAE5VQi5BUFdhdGNoZG9nAAAAAAAAAAAAAAAAAAAAAAAAfQAAAE5VQi5HUElPLklSUTYAAAAAAAAAAAAAAAAAAAAAAAAAgwAAAE5VQi5TUE1JMC5TVzMAAAAAAAAAAAAAAAAAAAAAAAAAiAAAAE5VQi5TUE1JMS5TVzMAAAAAAAAAAAAAAAAAAAAAAAAAjAAAAE5VQi5XYWtldXBBUAAAAAAAAAAAAAAAAAAAAAAAAAAAkQAAAFNNQy5DUFVXYWtldXBBUAAAAAAAAAAAAAAAAAAAAAAApQAAAFNNQy5PdXRib3hOb3RFbXB0eQAAAAAAAAAAAAAAAAAA0wAAAEFPUC5UcnVzdGVkT3V0Ym94Tm90RW1wdHkAAAAAAAAA7AAAAEFPUDIuQ1BVV2FrZXVwQVAAAAAAAAAAAAAAAAAAAAAA"
                 children: [
                   {
                     soc-tuner: {
                       device-set-0: [
-                        "4"
+                        "7"
                       ]
-                      device-set-1: 336
+                      device-set-1: 230
-                      device-set-10: 434
+                      device-set-10: 305
-                      device-set-2: "["
+                      device-set-2: ":"
-                      device-set-3: [
-                        "V"
-                        "W"
-                        "X"
-                        "Y"
-                      ]
+                      device-set-3: "ugAAALsAAAC8AAAAvQAAAL4AAAC/AAAA"
-                      device-set-5: 417
+                      device-set-5: null
-                      device-set-6: "]"
+                      device-set-6: "<"
-                      device-set-7: 342
+                      device-set-7: 236
-                      device-set-8: "b"
+                      device-set-8: "("
-                      device-set-9: 428
+                      device-set-9: 1241245548843
                       function-mcc_ctrl: [
                         ...
-                        ")"
+                        "("
                       ]
-                      mtp-clk-slowdown: 1
+                      mtp-clk-slowdown: 0
                     }
                   }
                   {
                     clpc: {
-                      cpu-amx-mem-llc-ld-miss-ki-down: 983040
-                      cpu-amx-mem-llc-ld-miss-ki-up: 1638400
-                      cpu-amx-mem-llc-ld-miss-target: 655
-                      cpu-eff-lpm-spl-ki-up-c0: "ff"
-                      cpu-eff-lpm-spl-ki-up-c1: 6553
-                      cpu-efficiency-lpm-enabled: 0
-                      cpu-efficiency-lpm-target: 6225
-                      events: [
-                        "S"
-                        "("
-                        "\""
-                        "#"
-                      ]
+                      clpc-dev-intrs-timeout: 2000000
+                      cpu-e-step-down-delay-us: 500
+                      cpu-high-e-threshold-high-p: 589824
+                      cpu-high-e-threshold-low-p: 327680
+                      cpu-upo-frequency-min-e: 1140
+                      cpu-utilization-control-mode: 3
+                      cpu-utilization-spl-ki-down-c0: 3604
+                      cpu-utilization-spl-ki-down-c1: 3604
+                      cpu-utilization-spl-ki-down-c2: 3604
+                      cpu-utilization-spl-ki-down-c3: 3604
+                      cpu-utilization-spl-ki-up-c0: 1376256
+                      cpu-utilization-spl-ki-up-c1: 131072
+                      cpu-utilization-spl-ki-up-c2: 851968
+                      cpu-utilization-spl-ki-up-c3: 622592
+                      cpu-utilization-spl-ki-up-t1: "16"
+                      cpu-utilization-spl-ki-up-t2: 17694
+                      dram-power-limit-spl-cpu-c0: 65536
+                      dram-power-limit-spl-cpu-c1: "ff"
+                      dram-power-limit-spl-cpu-c2: 19660
+                      dram-power-limit-spl-cpu-c3: "33"
+                      dram-power-limit-spl-cpu-t1: 19660
+                      dram-power-limit-spl-cpu-t2: 52428
+                      dram-power-limit-spl-gpu-c0: 65536
+                      dram-power-limit-spl-gpu-c1: "ff"
+                      dram-power-limit-spl-gpu-c2: 19660
+                      dram-power-limit-spl-gpu-c3: "33"
+                      dram-power-limit-spl-gpu-t1: 19660
+                      dram-power-limit-spl-gpu-t2: 52428
+                      dram-power-limit-spl-t0: 0
+                      dram-power-limit-spl-t3: 65536
+                      fab-compute-power-target-high: 3932
+                      fab-compute-power-target-low: 1966
+                      mem-cpu-stall-min-effort-c1-p: 65536
+                      mem-cpu-stall-min-effort-t1-p: 6553
+                      mem-cpu-stall-r-ki-down-c1-p: 131072
+                      mem-cpu-stall-r-ki-up-c1-p: 19660
+                      mem-cpu-stall-r-t1-p: 41549
+                      mem-cpu-stall-r-target2-p: 3276
-                      ane-utility-max-freq: 1320
+                      ane-utility-max-freq: 1332
-                      compatible: "clpc,t8130"
+                      compatible: "clpc,t8140"
-                      cpu-avg-limiter-ki: 50332
+                      cpu-avg-limiter-ki: 53687
-                      cpu-avg-limiter-kp: 1342177
+                      cpu-avg-limiter-kp: 1375732
-                      cpu-bg-limiter-target: 19661
+                      cpu-bg-limiter-target: "ff"
-                      interrupts: 710
+                      interrupts: 840
-                      pkg-avg-limiter-ki: 5872
+                      pkg-avg-limiter-ki: 5201
-                      pkg-power-limit-spl-cpu-t1: 1528824
+                      pkg-power-limit-spl-cpu-t1: 1530921
-                      pkg-power-limit-spl-cpu-t2: 1528824
+                      pkg-power-limit-spl-cpu-t2: 1530921
-                      pkg-power-limit-spl-gpu-t1: 1528824
+                      pkg-power-limit-spl-gpu-t1: 1530921
-                      pkg-power-limit-spl-gpu-t2: 1528824
+                      pkg-power-limit-spl-gpu-t2: 1530921
-                      pkg-power-limit-spl-t3: 1528824
+                      pkg-power-limit-spl-t3: 1530921
-                      pkg-power-zone-target-0: 209715
+                      pkg-power-zone-target-0: 255590
-                      pkg-sustainable-power-target: 196608
+                      pkg-sustainable-power-target: 219545
                     }
                   }
                   {
                     ppm: {
-                      cpms-input-Pu-cutoff-voltage: 212992
+                      brownout-risk-CE-lane: 6
+                      brownout-risk-CE-threshold: 49152
+                      brownout-risk-debounce-time: 5000
+                      cpms-input-pp-max-fusion: 1
+                      cpms-input-ratio-up-pp: 52428
+                      cpms-input-use-filter-pp: 1
+                      cpms-input-weight-factor-pp: 65536
                       client-predictive-horizon-pmax: [
                         ...
+                        "'"
+                        "'"
                         ...
-                        "2"
                       ]
-                      client-predictive-pmax-budgets: "AAALEJQRAABoEAAAPA8AABAOAADkDAAAuAsAAIwKAABgCQAANAgAAAgHAADcBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMNAAABAIe4AAC0fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
+                      client-predictive-pmax-budgets: "AAALEJQRAABoEAAAPA8AABAOAADkDAAAuAsAAIwKAABgCQAANAgAAAgHAADcBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMNAAABANfAAACQjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
-                      client-predictive-pmax-powers: "AAALEGQZAAA4GAAADBcAAOAVAAC0FAAAiBMAAFwSAAAwEQAABBAAANgOAACsDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMNTT4AADstAABZHgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
+                      client-predictive-pmax-powers: "AAALEGQZAAA4GAAADBcAAOAVAAC0FAAAiBMAAFwSAAAwEQAABBAAANgOAACsDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMNiUwAAKc5AAAGKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
-                      client_budgets_extra: "AAAAAwQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEDwAAAA4AAAANAAAADAAAAAsAAAAKAAAACQAAAAgAAAAHAAAABgAAAAUAAAAEAAAAAwAAAAIAAAABAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAQCHuAAAtHwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
+                      client_budgets_extra: "AAAAAwQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEDwAAAA4AAAANAAAADAAAAAsAAAAKAAAACQAAAAgAAAAHAAAABgAAAAUAAAAEAAAAAwAAAAIAAAABAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAQDXwAAAkIwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
-                      client_powers_extra: "AAAAA9gxAADYMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEwQYAABAIAAAQCAAAzAIAAPUDAABEBQAARAUAAGQAAADBBgAAEAgAABAIAADMAgAA9QMAAEQFAABEBQAAAAAAAAAAAAaCBQAAggUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADU0+AAA7LQAAWR4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
+                      client_powers_extra: "AAAAA+8uAADvLgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEwQYAABAIAAAQCAAAzAIAAPUDAABEBQAARAUAAGQAAADBBgAAEAgAABAIAADMAgAA9QMAAEQFAABEBQAAAAAAAAAAAAaCBQAAggUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYlMAACnOQAABioAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
                       cpms-batt-model-100ms-fallback: [
-                        "!5"
-                        "(p"
-                        "+d"
-                        "1Y"
-                        "2x"
-                        "4D"
-                        "9="
-                        "< "
-                        "B*"
-                        "C>"
-                        "E~"
-                        "HD"
-                        "I4"
-                        "I]"
-                        "If"
-                        "J|"
-                        "Kk"
-                        "Mu"
-                        "SA"
-                        "SH"
-                        "T/"
-                        "\\T"
-                        "^M"
-                        "d["
-                        "fg"
-                        "oq"
-                        "p;"
-                        "vw"
-                        "}L"
+                        ")P"
+                        "*1"
+                        "-H"
+                        "0<"
+                        "8-"
+                        "?8"
+                        "A("
+                        "A("
+                        "A:"
+                        "Jb"
+                        "KP"
+                        "O)"
+                        "Rd"
+                        "To"
+                        "Uz"
+                        "X"
+                        "__"
+                        "`&"
+                        "bZ"
+                        "g_"
+                        "g~"
+                        "h9"
+                        "iK"
+                        "jg"
+                        "r\""
+                        "u1"
+                        "v4"
+                        "y~"
+                        "{u"
+                        "}e"
+                        "~k"
                       ]
-                      cpms-batt-model-1ms-fallback: "QJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAL2mAABQswAAp8AAAPvLAADq1wAAm+QAALTsAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAN6EAAP6rAAAduwAAGsgAAIfVAADr4wAAM/IAAC8BAQCvDgEALRoBAECcAABAnAAAQJwAAECcAABAnAAAGJ0AAP+jAAAGqQAAu64AAAC2AACUvgAAgMsAAJ3dAACn7AAAJ/wAAMoMAQAqHgEARS8BALE+AQB0SwEAQJwAAECcAABAnAAAsKQAAEqvAAAPuAAAy78AAJjFAADoywAAndQAAOLdAAA+7QAAzQIBAAUUAQCiJQEAtTgBAJJNAQDnYAEAjnIBAIiAAQBAnAAAQJwAAJSyAABnwAAAXMwAAM7VAADw3gAAa+UAACLtAABQ9wAA0gIBAMgUAQDlLQEAZEEBAN1WAQDlbAEA0oQBAOSaAQCfrwEAA78BANesAADXrAAAGc0AAOfcAABK6gAAjvQAAKb/AADTBgEAHhABAOMbAQDwKQEAsT4BAMFbAQBWcQEAGYsBAFSkAQBMvwEAKdgBAP/vAQAXAQIAGcsAABnLAAAC6wAAO/sAAFsKAQC4FQEA6yIBABosAQBRNwEAJkUBAB9WAQBlbgEACZABACepAQDuxQEA/+MBALABAgDvHQIA8TYCAMpKAgCP5wAAj+cAANsIAQDuGQEAHCsBAKI3AQBDRwEAf1IBAKtfAQCGbwEAtIMBAK6fAQD8xQEA6eIBAJMCAgDAJQIAWUYCAARmAgBQgAIAPpcCAMICAQDCAgEA2iYBAN84AQBLTAEA71kBAENsAQCDeQEAoYgBAGKaAQAEsgEA0tEBAMv8AQDFHQIAG0ACAJdoAgBOjAIAZ68CADvLAgCZ5QIA+xwBAPscAQANRQEA3lcBAJ5tAQBBfAEAg5EBAKugAQCpsQEAJMUBAGrgAQAfBAIAsDMCAO1YAgCqfQIAj6sCAKDSAgAh+QIA0xYDAAU1AwBYNgEAWDYBAGFjAQCudgEAyo4BAD+eAQCbtgEAg8cBAEfaAQBB7wEATw4CAPE1AgD5aQIAqZMCAHa6AgDL7QIAcxgDAFRCAwBIYgMAtYQDAA=="
+                      cpms-batt-model-1ms-fallback: "QJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAECcAABAnAAAQJwAAA=="
                       cpms-batt-model-1s-fallback: [
-                        "#("
-                        "#1"
-                        "(V"
-                        "(`"
-                        "+A"
-                        ",c"
-                        ".c"
-                        "3?"
-                        "6@"
-                        "7="
-                        "7g"
-                        "8y"
-                        "9{"
+                        "#%"
+                        "#R"
+                        "(Y"
+                        "+;"
+                        ",8"
+                        ",x"
+                        "1$"
+                        "1G"
+                        "2N"
+                        "4x"
                         ...
-                        "<;"
-                        "=P"
-                        "C\\"
-                        "G&"
-                        "H]"
-                        "P!"
-                        "V="
-                        "V="
-                        "mG"
-                        "mn"
-                        "y6"
+                        ":k"
+                        "=d"
+                        "?-"
+                        "A3"
+                        "A:"
+                        "Ad"
+                        "C7"
+                        "Cb"
+                        "D'"
+                        "L:"
+                        "LJ"
+                        "Y/"
+                        "YL"
+                        "[U"
+                        "^W"
+                        "_+"
+                        "bQ"
+                        "cx"
+                        "eC"
+                        "eh"
+                        "oH"
+                        "qp"
+                        "u*"
+                        "xS"
+                        "yD"
                       ]
-                      cpms-dt-curve: "AAAAAAAAAAAAAAAAAQAAAFgAAACLAAAArwAAANIAAADsAAAA/wAAAJEfAAAvEwAAHhAAALQLAACXCAAA5AUAANADAAAIAgAAZGlzcGxheQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAACDAAAAvAAAAOcAAAD/AAAAAAAAAAAAAACwHQAAwxsAAHEYAAAHEwAAKgwAAPAGAAAAAAAAAAAAAGhhcHRpY3MAAAAAAAAAAAABAAAAAAAAAAAAAAABAAAALAAAAFQAAACtAAAA/wAAAAAAAAAAAAAAECcAAIAMAAD8CAAACAcAAEwEAACQAQAAAAAAAAAAAABiYXNlYmFuZAAAAAAAAAAAAQAAAAAAAAAAAAAAAQAAAEYAAAB/AAAAmgAAANMAAADwAAAA/wAAAOj9AAAqJwAAsh8AACAYAAA/FAAAUwwAAEUIAABYBgAAcGFja2FnZQAAAAAAAAAAAAIAAAAAAAAAAAAAAAEAAAAnAAAATQAAAHgAAACnAAAA1AAAAP8AAACRHwAALxMAAB8QAAC1CwAAlwgAAOQFAADQAwAACAIAAGRpc3BsYXkAAAAAAAAAAAACAAAAAAAAAAAAAAABAAAAewAAAMAAAADvAAAA/wAAAAAAAAAAAAAA/w4AALUMAADZCgAALwgAAKwEAAC0AgAAAAAAAAAAAABoYXB0aWNzAAAAAAAAAAAAAgAAAAEAAAAAAAAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIFAACCBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbmFuZAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAEAAAA5AAAAcQAAAIwAAADLAAAA7QAAAP8AAADo/QAAKicAALIfAAAgGAAAPxQAAFMMAABFCAAAWAYAAHBhY2thZ2UAAAAAAAAAAAACAAAAAAAAAAAAAAABAAAAFgAAAFoAAACNAAAAvwAAAP8AAAAAAAAAKw0AAMMKAAD5CAAAtQYAAHQFAADcAwAAvwIAAAAAAAB3aWZpAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAQAAADIAAABbAAAAhgAAALEAAADaAAAA/wAAAJEfAAAvEwAAHxAAALULAACXCAAA5AUAANADAAAIAgAAZGlzcGxheQAAAAAAAAAAAAMAAAAAAAAAAAAAAAEAAABTAAAA/wAAAAAAAAAAAAAAAAAAAAAAAACUEQAAlBEAAJQRAADcBQAAAAAAAAAAAAAAAAAAAAAAAGlvcG9ydAAAAAAAAAAAAAADAAAAAAAAAAAAAAABAAAANwAAAG0AAACHAAAAxwAAAO0AAAD/AAAA6P0AAHsiAAA2GwAAFxQAAJYQAACgCQAAPQYAAEQFAABwYWNrYWdlAAAAAAAAAAAAAwAAAAAAAAAAAAAAAQAAAFwAAACrAAAA/wAAAAAAAAAAAAAAAAAAAFwcAADLCAAAhgYAANUEAABnAwAAAAAAAAAAAAAAAAAAc3BlYWtlcgAAAAAAAAAAAAQAAAAAAAAAAAAAAAEAAAAuAAAAZQAAAIAAAADEAAAA6AAAAP8AAADo/QAAIFsAAOFMAADCOwAAaTMAAIUeAABSEwAAMAwAAHBhY2thZ2UAAAAAAAAAAAA="
+                      cpms-dt-curve: "AAAAAAAAAAAAAAAAAQAAAD0AAABmAAAAjgAAALkAAADfAAAA/wAAAPcWAADGCwAANwoAAN0HAAAKBgAAPAQAAMoCAAB+AQAAZGlzcGxheQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAB3AAAAzAAAAP8AAAAAAAAAAAAAAAAAAAB9GQAAfhcAAGYTAAAiDAAAAQYAAAAAAAAAAAAAAAAAAGhhcHRpY3MAAAAAAAAAAAABAAAAAAAAAAAAAAABAAAALAAAAFQAAACtAAAA/wAAAAAAAAAAAAAAECcAAIAMAAD+CAAACQcAAEwEAACQAQAAAAAAAAAAAABiYXNlYmFuZAAAAAAAAAAAAQAAAAAAAAAAAAAAAQAAAEUAAAB/AAAAmgAAANQAAADwAAAA/wAAAOj9AADhLAAA9CMAAPIaAABpFgAAMA0AAJkIAABYBgAAcGFja2FnZQAAAAAAAAAAAAIAAAAAAAAAAAAAAAEAAAAkAAAAQwAAAGoAAACbAAAAywAAAP8AAAD3FgAAxgsAADcKAADcBwAACgYAADwEAADKAgAAfgEAAGRpc3BsYXkAAAAAAAAAAAACAAAAAAAAAAAAAAABAAAAeAAAALcAAADpAAAA/wAAAAAAAAAAAAAA6QwAAPgKAABvCQAAeQcAAKwEAAC8AgAAAAAAAAAAAABoYXB0aWNzAAAAAAAAAAAAAgAAAAEAAAAAAAAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIFAACCBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbmFuZAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAEAAAAzAAAAZwAAAIQAAADIAAAA7AAAAP8AAADo/QAA4SwAAPQjAADyGgAAaRYAADANAACZCAAAWAYAAHBhY2thZ2UAAAAAAAAAAAACAAAAAAAAAAAAAAABAAAAEwAAAEoAAAB4AAAAtwAAAP8AAAAAAAAAYAoAAMoJAADYBwAA8AUAABUFAAAZAwAAGAIAAAAAAAB3aWZpAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAQAAADIAAABUAAAAewAAAKgAAADTAAAA/wAAAPcWAADGCwAANwoAANwHAAAKBgAAPAQAAMoCAAB+AQAAZGlzcGxheQAAAAAAAAAAAAMAAAAAAAAAAAAAAAEAAABOAAAA/wAAAAAAAAAAAAAAAAAAAAAAAACUEQAAlBEAAJQRAADcBQAAAAAAAAAAAAAAAAAAAAAAAGlvcG9ydAAAAAAAAAAAAAADAAAAAAAAAAAAAAABAAAANAAAAGUAAAB/AAAAwwAAAOwAAAD/AAAA6P0AAHAmAACCHgAAehYAAHoSAABsCgAAjQYAAEQFAABwYWNrYWdlAAAAAAAAAAAAAwAAAAAAAAAAAAAAAQAAAIsAAADQAAAA/wAAAAAAAAAAAAAAAAAAACgjAACMCgAAjggAANgGAAB4BQAAAAAAAAAAAAAAAAAAc3BlYWtlcgAAAAAAAAAAAAQAAAAAAAAAAAAAAAEAAAAuAAAAZQAAAIEAAADEAAAA6AAAAP8AAADo/QAAQFsAAN9MAADdOwAAZTMAAHoeAABLEwAAMAwAAHBhY2thZ2UAAAAAAAAAAAA="
-                      cpms-dt-topology: "AAAAAMv3DDtW8Fs6AQAAAHNwaWtlX3Bvd2VyLmkAAAABAAAAJgD/O2joHzpkAAAAc3Bpa2VfcG93ZXIuZgAAAAIAAADB/ms7aOifOWQAAABzcGlrZV9wb3dlci5zAAAAAwAAABKDwDswZWA56AMAAHNwaWtlX3Bvd2VyLnMAAAAEAAAAAAAAAAAAAAABAAAAZHJvb3AAAAAAAAAAAAAAAAUAAAAQBMg6Wg50OugDAABzcGlrZV9wb3dlci5mAAAA"
+                      cpms-dt-topology: "AAAAAAAAAAByM1w6AQAAAHNwaWtlX3Bvd2VyLmkAAAABAAAAAAAAAFhzADpkAAAAc3Bpa2VfcG93ZXIuZgAAAAIAAAAAAAAAWHOAOWQAAABzcGlrZV9wb3dlci5zAAAAAwAAAAAAAABYc4A56AMAAHNwaWtlX3Bvd2VyLnMAAAAEAAAAAAAAAAAAAAABAAAAZHJvb3AAAAAAAAAAAAAAAAUAAAAQBMg6Wg50OugDAABzcGlrZV9wb3dlci5uAAAABgAAAAAAAABvEoM66AMAAHNwaWtlX3Bvd2VyLmUAAAA="
-                      cpms-full-mode-load-fraction: 32768
+                      cpms-full-mode-load-fraction: 49152
-                      interrupts: 711
+                      interrupts: 841
-                      systemloadinput-ptle-rank-pp: "Y"
+                      systemloadinput-ptle-rank-pp: "U"
-                      systemloadinput-ptle-rank-ps: "Y"
+                      systemloadinput-ptle-rank-ps: "Z"
                     }
                   }
                 ]
-                compatible: "pmgr1,t8130"
+                compatible: "pmgr1,t8140"
-                device-check-ps-b4-sleep: "AAAAAYMAhwCIAIYAiQCKAIsAjACEAIUAUgAAAAAAAAAAAAAAAAAAAmQAZQBmAGkAagAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
+                device-check-ps-b4-sleep: [
+                  "O"
+                  "`"
+                  "_"
+                ]
                 devices: [
                   {
-                    map: 7
-                    name: "ECPU0"
+                    name: "ECPU_0"
                   }
-                  {
-                    flag: 1
-                    index: 1
-                    map: 8
-                    id2: 16
-                    name: "MSG"
-                  }
-                  {
-                    flag: 16
-                    alias: 100
-                    index: 27
-                    map: 10
-                    id2: 106
-                    name: "DPEXT"
-                  }
-                  {
-                    flag: 41
-                    index: 0
-                    map: 11
-                    id2: 107
-                    unk4: 15
-                    name: "SEP"
-                  }
                   {
-                    map: 12
+                    unk2: 16384
-                    alias: 52
+                    alias: 55
-                    id2: 108
+                    id2: 106
                   }
-                  {
-                    flag: 32
-                    alias: 108
-                    index: 1
-                    map: 12
-                    id2: 109
-                    name: "ISP_CPU_CORE0"
-                  }
-                  {
-                    flag: 32
-                    alias: 108
-                    index: 2
-                    map: 12
-                    id2: 110
-                    name: "ISP_CPU_CORE1"
-                  }
-                  {
-                    alias: 52
-                    index: 3
-                    map: 12
-                    id2: 111
-                    name: "ISP_FE"
-                  }
                   {
-                    map: 12
+                    unk2: 16416
-                    alias: 111
+                    alias: 109
-                    index: 4
+                    index: 0
-                    id2: 112
+                    id2: 110
                   }
                   {
-                    map: 12
+                    unk2: 16424
-                    alias: 111
+                    alias: 109
-                    index: 5
+                    index: 0
-                    id2: 113
+                    id2: 111
                   }
-                  {
-                    alias: 111
-                    index: 6
-                    map: 12
-                    id2: 114
-                    name: "ISP_STS0"
-                  }
-                  {
-                    alias: 111
-                    index: 7
-                    map: 12
-                    id2: 115
-                    name: "ISP_STS1"
-                  }
-                  {
-                    flag: 1
-                    index: 2
-                    map: 8
-                    id2: 17
-                    name: "AIC"
-                  }
-                  {
-                    alias: 111
-                    index: 8
-                    map: 12
-                    id2: 116
-                    name: "ISP_PEARL"
-                  }
-                  {
-                    alias: 111
-                    index: 9
-                    map: 12
-                    id2: 117
-                    name: "ISP_BE"
-                  }
                   {
-                    map: 12
+                    unk2: 16480
-                    index: 10
+                    index: 0
-                    name: "ISP_CLR"
+                    name: "ISP_CVM"
                   }
-                  {
-                    alias: 117
-                    index: 11
-                    map: 12
-                    id2: 119
-                    name: "ISP_CVD"
-                  }
                   {
-                    map: 12
+                    unk2: 32776
-                    index: 12
+                    index: 0
-                    name: "ISP_CVM"
+                    name: "VENC0_PIPE4"
                   }
                   {
-                    map: 13
+                    unk2: 32784
-                    alias: 45
+                    alias: 119
-                    name: "VENC_DMA"
+                    name: "VENC0_PIPE5"
                   }
                   {
-                    map: 13
+                    unk2: 32792
-                    alias: 121
+                    alias: 119
-                    index: 1
+                    index: 0
-                    name: "VENC_PIPE4"
+                    name: "VENC0_ME0"
                   }
                   {
-                    map: 13
+                    unk2: 32800
-                    alias: 121
+                    alias: 122
-                    index: 2
+                    index: 0
-                    name: "VENC_PIPE5"
+                    name: "VENC0_ME1"
                   }
                   {
-                    map: 13
+                    unk2: 32808
-                    alias: 121
+                    alias: 51
-                    index: 3
+                    index: 0
-                    name: "VENC_ME0"
+                    name: "VENC1_DMA"
                   }
                   {
-                    map: 13
+                    unk2: 32816
-                    index: 4
+                    index: 0
-                    name: "VENC_ME1"
+                    name: "VENC1_PIPE4"
                   }
-                  {
-                    flag: 1
-                    index: 3
-                    map: 8
-                    id2: 18
-                    name: "DWI"
-                  }
-                  {
-                    flag: 48
-                    alias: 93
-                    index: 1
-                    map: 14
-                    id2: 127
-                    name: "ANE_CPU"
-                  }
                   {
-                    flag: 32
-                    map: 15
+                    unk2: 65536
-                    alias: 96
+                    alias: 77
-                    unk1: 655360
+                    unk1: 251658240
-                    id2: 130
+                    id2: 132
                   }
-                  {
-                    flag: 16
-                    alias: 96
-                    index: 1
-                    map: 15
-                    id2: 131
-                    name: "DISP_BE"
-                  }
-                  {
-                    flag: 16
-                    alias: 131
-                    index: 2
-                    map: 15
-                    id2: 132
-                    name: "DP"
-                  }
-                  {
-                    flag: 16
-                    alias: 131
-                    index: 2
-                    map: 15
-                    id2: 133
-                    name: "MIPI_DSI"
-                  }
-                  {
-                    flag: 16
-                    alias: 131
-                    index: 3
-                    map: 15
-                    id2: 134
-                    name: "DISP_DSC"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 4
-                    map: 15
-                    id2: 135
-                    name: "DISP_GP0"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 5
-                    map: 15
-                    id2: 136
-                    name: "DISP_GP1"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 6
-                    map: 15
-                    id2: 137
-                    name: "DISP_CMB"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 7
-                    map: 15
-                    id2: 138
-                    name: "DISP_PPP"
-                  }
-                  {
-                    flag: 1
-                    index: 4
-                    map: 8
-                    id2: 19
-                    name: "GPIO"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 8
-                    map: 15
-                    id2: 139
-                    name: "DISP_HILO"
-                  }
-                  {
-                    flag: 48
-                    alias: 96
-                    index: 9
-                    map: 15
-                    id2: 140
-                    name: "DISP_ITL"
-                  }
                   {
+                    unk2: 16777216
-                    id2: 256
+                    id2: 141
                   }
-                  {
-                    flag: 41
-                    index: 11
-                    id2: 257
-                    name: "NUB_SPMI0"
-                  }
-                  {
-                    flag: 41
-                    index: 12
-                    id2: 258
-                    name: "NUB_SPMI1"
-                  }
-                  {
-                    flag: 41
-                    index: 13
-                    id2: 259
-                    name: "NUB_SPMI_A0"
-                  }
-                  {
-                    flag: 41
-                    index: 14
-                    id2: 260
-                    name: "NUB_AON"
-                  }
-                  {
-                    flag: 9
-                    index: 15
-                    id2: 261
-                    name: "NUB_SPI0"
-                  }
                   {
+                    unk2: 16777344
-                    index: 16
+                    index: 0
-                    id2: 262
+                    id2: 147
                   }
                   {
+                    unk2: 16777352
-                    index: 17
+                    index: 0
-                    id2: 263
+                    id2: 148
                   }
-                  {
-                    flag: 41
-                    index: 5
-                    map: 8
-                    id2: 20
-                    name: "PMS_BUSIF"
-                  }
-                  {
-                    flag: 41
-                    index: 18
-                    id2: 264
-                    name: "NUB_FABRIC"
-                  }
-                  {
-                    flag: 41
-                    index: 19
-                    id2: 265
-                    name: "NUB_SRAM"
-                  }
-                  {
-                    flag: 41
-                    index: 20
-                    id2: 266
-                    name: "DEBUG_SWITCH"
-                  }
-                  {
-                    flag: 48
-                    index: 0
-                    map: 1
-                    id2: 267
-                    name: "AOP_FILTER"
-                  }
-                  {
-                    flag: 16
-                    index: 1
-                    map: 1
-                    id2: 268
-                    name: "AOP_GPIO"
-                  }
-                  {
-                    flag: 48
-                    index: 2
-                    map: 1
-                    id2: 269
-                    name: "AOP_BASE"
-                  }
-                  {
-                    flag: 16
-                    index: 3
-                    map: 1
-                    id2: 270
-                    name: "AOP_FR"
-                  }
-                  {
-                    flag: 48
-                    index: 4
-                    map: 1
-                    id2: 271
-                    name: "AOP_LEAP_CLK"
-                  }
-                  {
-                    flag: 16
-                    index: 5
-                    map: 1
-                    id2: 272
-                    name: "AOP_SHIM"
-                  }
-                  {
-                    flag: 16
-                    index: 6
-                    map: 1
-                    id2: 273
-                    name: "AOP_ADMA0"
-                  }
-                  {
-                    flag: 41
-                    index: 6
-                    map: 8
-                    id2: 21
-                    name: "PMS"
-                  }
-                  {
-                    flag: 16
-                    index: 7
-                    map: 1
-                    id2: 274
-                    name: "AOP_PIODMA"
-                  }
-                  {
-                    flag: 48
-                    index: 8
-                    map: 1
-                    id2: 275
-                    name: "AOP_CPU"
-                  }
-                  {
-                    flag: 16
-                    index: 9
-                    map: 1
-                    id2: 276
-                    name: "AOP_I2CM0"
-                  }
-                  {
-                    flag: 16
-                    index: 10
-                    map: 1
-                    id2: 277
-                    name: "AOP_I2CM1"
-                  }
-                  {
-                    flag: 16
-                    index: 11
-                    map: 1
-                    id2: 278
-                    name: "AOP_I2CM2"
-                  }
-                  {
-                    flag: 16
-                    index: 12
-                    map: 1
-                    id2: 279
-                    name: "AOP_I2CM3"
-                  }
-                  {
-                    flag: 48
-                    index: 13
-                    map: 1
-                    id2: 280
-                    name: "AOP_SCM"
-                  }
-                  {
-                    flag: 16
-                    index: 14
-                    map: 1
-                    id2: 281
-                    name: "AOP_SPI0"
-                  }
-                  {
-                    flag: 16
-                    index: 15
-                    map: 1
-                    id2: 282
-                    name: "AOP_SPI1"
-                  }
-                  {
-                    flag: 48
-                    index: 16
-                    map: 1
-                    id2: 283
-                    name: "AOP_SPMI0"
-                  }
-                  {
-                    flag: 1
-                    index: 7
-                    map: 8
-                    id2: 22
-                    name: "PMS_FPWM0"
-                  }
-                  {
-                    flag: 48
-                    index: 17
-                    map: 1
-                    id2: 284
-                    name: "AOP_SPMI1"
-                  }
-                  {
-                    flag: 16
-                    index: 18
-                    map: 1
-                    id2: 285
-                    name: "AOP_HE_NRCS0"
-                  }
-                  {
-                    flag: 16
-                    index: 19
-                    map: 1
-                    id2: 286
-                    name: "AOP_HE_NRCS1"
-                  }
-                  {
-                    flag: 16
-                    index: 20
-                    map: 1
-                    id2: 287
-                    name: "AOP_LEAP"
-                  }
-                  {
-                    flag: 16
-                    index: 21
-                    map: 1
-                    id2: 288
-                    name: "AOP_AUDIO_SHIM"
-                  }
-                  {
-                    flag: 16
-                    index: 22
-                    map: 1
-                    id2: 289
-                    name: "AOP_AUDIO_ADMA0"
-                  }
-                  {
-                    flag: 16
-                    index: 23
-                    map: 1
-                    id2: 290
-                    name: "AOP_UART0"
-                  }
-                  {
-                    flag: 16
-                    index: 24
-                    map: 1
-                    id2: 291
-                    name: "AOP_UART1"
-                  }
-                  {
-                    flag: 16
-                    index: 25
-                    map: 1
-                    id2: 292
-                    name: "AOP_UART2"
-                  }
-                  {
-                    flag: 16
-                    index: 26
-                    map: 1
-                    id2: 293
-                    name: "AOP_MCA0"
-                  }
-                  {
-                    flag: 1
-                    index: 8
-                    map: 8
-                    id2: 23
-                    name: "PMS_FPWM1"
-                  }
-                  {
-                    flag: 16
-                    index: 27
-                    map: 1
-                    id2: 294
-                    name: "AOP_MCA1"
-                  }
-                  {
-                    flag: 16
-                    index: 28
-                    map: 1
-                    id2: 295
-                    name: "AOP_MCA2"
-                  }
-                  {
-                    flag: 16
-                    index: 29
-                    map: 1
-                    id2: 296
-                    name: "AOP_MCA3"
-                  }
-                  {
-                    flag: 16
-                    index: 30
-                    map: 1
-                    id2: 297
-                    name: "AOP_PDMC0"
-                  }
-                  {
-                    flag: 48
-                    index: 31
-                    map: 1
-                    id2: 298
-                    name: "AOP_SRAM"
-                  }
-                  {
-                    flag: 16
-                    index: 0
-                    map: 2
-                    id2: 299
-                    name: "AOP_PDM0_REF"
-                  }
-                  {
-                    flag: 16
-                    index: 1
-                    map: 2
-                    id2: 300
-                    name: "AOP_PDM1_REF"
-                  }
-                  {
-                    flag: 48
-                    index: 0
-                    map: 3
-                    id2: 301
-                    name: "SMC_FABRIC"
-                  }
-                  {
-                    flag: 16
-                    index: 1
-                    map: 3
-                    id2: 302
-                    name: "SMC_GPIO"
-                  }
-                  {
-                    flag: 48
-                    index: 2
-                    map: 3
-                    id2: 303
-                    name: "SMC_AON"
-                  }
-                  {
-                    flag: 1
-                    index: 9
-                    map: 8
-                    id2: 24
-                    name: "PMS_FPWM2"
-                  }
-                  {
-                    flag: 16
-                    index: 3
-                    map: 3
-                    id2: 304
-                    name: "SMC_UART0"
-                  }
-                  {
-                    flag: 16
-                    index: 4
-                    map: 3
-                    id2: 305
-                    name: "SMC_UART1"
-                  }
-                  {
-                    flag: 1
-                    index: 5
-                    map: 3
-                    id2: 306
-                    name: "SMC_I2CM0"
-                  }
-                  {
-                    flag: 1
-                    index: 6
-                    map: 3
-                    id2: 307
-                    name: "SMC_I2CM1"
-                  }
-                  {
-                    flag: 1
-                    index: 7
-                    map: 3
-                    id2: 308
-                    name: "SMC_I2CM2"
-                  }
-                  {
-                    flag: 16
-                    index: 8
-                    map: 3
-                    id2: 309
-                    name: "SMC_FPWM0"
-                  }
-                  {
-                    flag: 16
-                    index: 9
-                    map: 3
-                    id2: 310
-                    name: "SMC_FPWM1"
-                  }
-                  {
-                    flag: 48
-                    index: 10
-                    map: 3
-                    id2: 311
-                    name: "SMC_CPU"
-                  }
-                  {
-                    flag: 16
-                    index: 11
-                    map: 3
-                    id2: 312
-                    name: "SMC_PTD"
-                  }
-                  {
-                    flag: 16
-                    index: 12
-                    map: 3
-                    id2: 313
-                    name: "NUB_HE_NRCS0"
-                  }
-                  {
-                    flag: 1
-                    index: 10
-                    map: 8
-                    id2: 25
-                    name: "PMS_FPWM3"
-                  }
-                  {
-                    flag: 16
-                    index: 13
-                    map: 3
-                    id2: 314
-                    name: "NUB_HE_NRCS1"
-                  }
-                  {
-                    flag: 48
-                    index: 0
-                    map: 4
-                    id2: 315
-                    name: "MTP_FABRIC"
-                  }
-                  {
-                    flag: 16
-                    index: 1
-                    map: 4
-                    id2: 316
-                    name: "MTP_GPIO"
-                  }
-                  {
-                    flag: 48
-                    index: 2
-                    map: 4
-                    id2: 317
-                    name: "MTP_BASE"
-                  }
-                  {
-                    flag: 16
-                    index: 3
-                    map: 4
-                    id2: 318
-                    name: "MTP_PERIPH"
-                  }
-                  {
-                    flag: 16
-                    index: 4
-                    map: 4
-                    id2: 319
-                    name: "MTP_UART0"
-                  }
-                  {
-                    flag: 48
-                    index: 5
-                    map: 4
-                    id2: 320
-                    name: "MTP_CPU"
-                  }
-                  {
-                    flag: 48
-                    index: 6
-                    map: 4
-                    id2: 321
-                    name: "MTP_SCM_FABRIC"
-                  }
-                  {
-                    flag: 48
-                    index: 7
-                    map: 4
-                    id2: 322
-                    name: "MTP_SPI0"
-                  }
-                  {
-                    flag: 16
-                    index: 8
-                    map: 4
-                    id2: 323
-                    name: "MTP_I2CM0"
-                  }
                   {
-                    map: 7
+                    unk2: 8
-                    index: 1
+                    index: 0
-                    name: "ECPU1"
+                    name: "ECPU_1"
                   }
-                  {
-                    flag: 1
-                    index: 11
-                    map: 8
-                    id2: 26
-                    name: "PMS_FPWM4"
-                  }
-                  {
-                    flag: 48
-                    index: 9
-                    map: 4
-                    id2: 324
-                    name: "MTP_SRAM"
-                  }
-                  {
-                    flag: 16
-                    index: 10
-                    map: 4
-                    id2: 325
-                    name: "MTP_DMA"
-                  }
-                  {
-                    flag: 16
-                    index: 0
-                    map: 5
-                    id2: 326
-                    name: "DSG"
-                  }
-                  {
-                    flag: 16
-                    index: 0
-                    map: 6
-                    id2: 327
-                    name: "HPD"
-                  }
                   {
-                    id2: 336
+                    id2: 230
                   }
                   {
-                    id2: 337
+                    id2: 231
                   }
                   {
-                    id2: 338
+                    id2: 232
                   }
                   {
-                    id2: 339
+                    id2: 233
                   }
                   {
-                    id2: 340
+                    id2: 234
                   }
                   {
-                    alias: 98
+                    alias: 40
-                    id2: 341
+                    id2: 235
                   }
-                  {
-                    flag: 1
-                    index: 12
-                    map: 8
-                    id2: 27
-                    name: "PMS_C1PPT"
-                  }
                   {
-                    id2: 342
+                    id2: 236
                   }
                   {
-                    alias: 98
+                    alias: 40
-                    id2: 343
+                    id2: 237
                   }
                   {
-                    id2: 344
+                    id2: 238
                   }
                   {
-                    id2: 345
+                    id2: 239
                   }
                   {
-                    id2: 346
+                    id2: 240
                   }
                   {
-                    id2: 347
+                    id2: 241
                   }
                   {
-                    id2: 348
+                    id2: 242
                   }
                   {
-                    id2: 349
+                    id2: 243
                   }
                   {
+                    alias: 21102637
+                    unk2: 576
-                    flag: 82
+                    flag: 2
-                    id2: 384
+                    id2: 50
-                    name: "VENC-AVE-VNOM"
+                    name: "VENC0_SYS"
                   }
-                  {
-                    flag: 16
-                    index: 0
-                    id2: 385
-                    name: "VENC-MEM-FAST"
-                  }
                   {
-                    map: 8
+                    unk2: 368
-                    index: 13
+                    index: 0
-                    id2: 28
+                    id2: 24
                   }
-                  {
-                    flag: 82
-                    id1: 10
-                    index: 0
-                    id2: 386
-                    name: "VENC-AVE-VMAX"
-                  }
                   {
+                    alias: 21102637
+                    unk2: 584
-                    flag: 82
+                    flag: 2
-                    id2: 387
+                    id2: 51
-                    name: "AVD-SOC-VNOM"
+                    name: "VENC1_SYS"
                   }
-                  {
-                    flag: 82
-                    id1: 11
-                    index: 0
-                    id2: 388
-                    name: "AVD-SOC-VMAX"
-                  }
                   {
+                    alias: 45
+                    unk2: 568
-                    flag: 82
+                    flag: 2
-                    id2: 389
+                    id2: 49
-                    name: "JPG-SOC-VNOM"
+                    name: "MSR"
                   }
-                  {
-                    flag: 82
-                    id1: 13
-                    index: 0
-                    id2: 390
-                    name: "JPG-SOC-VMAX"
-                  }
                   {
-                    flag: 82
+                    flag: 18
-                    id2: 391
+                    id2: 254
                   }
                   {
-                    flag: 82
+                    flag: 18
-                    id2: 392
+                    id2: 255
                   }
-                  {
-                    flag: 80
-                    index: 0
-                    id2: 393
-                    name: "CLPC-SOC-VNOM"
-                  }
-                  {
-                    flag: 80
-                    index: 0
-                    id2: 394
-                    name: "CLPC-SOC-VMAX"
-                  }
                   {
-                    id2: 395
+                    id2: 258
                   }
-                  {
-                    flag: 9
-                    index: 14
-                    map: 8
-                    id2: 29
-                    name: "SOC_DPE"
-                  }
                   {
-                    id2: 396
+                    id2: 259
                   }
                   {
-                    id1: 14
+                    id1: 15
-                    id2: 397
+                    id2: 260
                   }
                   {
-                    id2: 398
+                    id2: 252
-                    name: "PRORES-SOC-VMAX"
+                    name: "JPG-SOC-VNOM"
                   }
                   {
-                    id1: 12
+                    id1: 13
-                    id2: 399
+                    id2: 262
                   }
                   {
-                    id2: 400
+                    id2: 250
-                    name: "MSR-SOC-VMAX"
+                    name: "AVD-SOC-VNOM"
                   }
                   {
-                    id1: 18
+                    id1: 10
-                    id2: 436
+                    id2: 247
-                    name: "ATC0-SOC-VNOM"
+                    name: "VENC0-AVE-VNOM"
                   }
                   {
-                    alias: 55
+                    alias: 63
-                    id2: 416
+                    id2: 288
                   }
                   {
-                    id2: 417
+                    id2: 289
                   }
                   {
+                    unk2: 3072
-                    flag: 16
+                    flag: 9
-                    id2: 418
+                    id2: 105
-                    name: "VENC-SYS-V"
+                    name: "SEP"
                   }
                   {
-                    alias: 46
+                    alias: 56
-                    id2: 419
+                    id2: 290
                   }
                   {
-                    map: 8
+                    unk2: 384
-                    index: 15
+                    index: 0
-                    id2: 30
+                    id2: 26
                   }
                   {
-                    alias: 93
+                    alias: 60
-                    id2: 420
+                    id2: 291
                   }
                   {
-                    alias: 43
+                    alias: 48
-                    id2: 421
+                    id2: 292
                   }
                   {
-                    alias: 43
+                    alias: 48
-                    id2: 422
+                    id2: 293
                   }
                   {
-                    alias: 44
+                    alias: 49
-                    id2: 423
+                    id2: 294
                   }
                   {
-                    alias: 52
+                    alias: 55
-                    id2: 424
+                    id2: 295
                   }
                   {
-                    alias: 7209069
+                    alias: 7077995
-                    id2: 435
+                    id2: 309
                   }
                   {
-                    id2: 425
+                    id2: 248
-                    name: "SEP-PEARL-V"
+                    name: "VENC0-MEM-FAST"
                   }
                   {
-                    alias: 66
+                    alias: 180
-                    id2: 426
+                    id2: 297
                   }
                   {
-                    alias: 417
+                    alias: 289
-                    id2: 427
+                    id2: 298
                   }
                   {
-                    id2: 428
+                    id2: 299
                   }
-                  {
-                    flag: 32
-                    index: 16
-                    map: 8
-                    id2: 31
-                    name: "ISPSENS0"
-                  }
                   {
-                    alias: 36
+                    alias: 102
-                    id2: 429
+                    id2: 300
                   }
                   {
-                    id2: 434
+                    id2: 305
                   }
                   {
-                    id2: 350
+                    id2: 244
                   }
                   {
-                    id2: 351
+                    id2: 245
                   }
                   {
-                    id2: 352
+                    id2: 246
                   }
                   {
-                    alias: 130
+                    alias: 132
-                    id2: 430
+                    id2: 301
                   }
                   {
-                    alias: 99
+                    alias: 79
-                    id2: 431
+                    id2: 302
                   }
-                  {
-                    flag: 17
-                    alias: 104
-                    index: 0
-                    id2: 432
-                    name: "ATC0_USB-V"
-                  }
                   {
-                    id2: 433
+                    id2: 304
                   }
                   {
-                    id2: 448
+                    id2: 320
                   }
-                  {
-                    flag: 32
-                    index: 17
-                    map: 8
-                    id2: 32
-                    name: "ISPSENS1"
-                  }
-                  {
-                    flag: 41
-                    index: 18
-                    map: 8
-                    id2: 33
-                    unk4: 17
-                    name: "AMCC0"
-                  }
-                  {
-                    index: 19
-                    map: 8
-                    id2: 34
-                    name: "AFT0"
-                  }
-                  {
-                    flag: 41
-                    alias: 33
-                    index: 20
-                    map: 8
-                    id2: 35
-                    name: "DCS0"
-                  }
+                  {
+                    index: 0
+                    unk2: 96
+                    id2: 9
+                    name: "SEP_AON"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 256
+                    id2: 10
+                    name: "SBR"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 264
+                    id2: 11
+                    name: "MSG"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 272
+                    id2: 12
+                    name: "AIC"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 280
+                    id2: 13
+                    name: "DWI"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 288
+                    id2: 14
+                    name: "GPIO"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 296
+                    id2: 15
+                    name: "PMS_BUSIF"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 304
+                    id2: 16
+                    name: "PMS"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 312
+                    id2: 17
+                    name: "PMC"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 320
+                    id2: 18
+                    name: "PMS_FPWM0"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 328
+                    id2: 19
+                    name: "PMS_FPWM1"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 336
+                    id2: 20
+                    name: "PMS_FPWM2"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 344
+                    id2: 21
+                    name: "PMS_FPWM3"
+                  }
+                  {
+                    flag: 1
+                    index: 0
+                    unk2: 352
+                    id2: 22
+                    name: "PMS_FPWM4"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 360
+                    id2: 23
+                    name: "PMS_C1PPT"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 376
+                    id2: 25
+                    name: "SOC_DPE"
+                  }
+                  {
+                    index: 0
+                    unk2: 392
+                    id2: 27
+                    name: "ISPSENS0"
+                  }
+                  {
+                    index: 0
+                    unk2: 400
+                    id2: 28
+                    name: "ISPSENS1"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 408
+                    id2: 29
+                    name: "AFIMCCNI0"
+                  }
+                  {
+                    index: 0
+                    unk2: 424
+                    id2: 31
+                    name: "PIOGW"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 432
+                    id2: 32
+                    name: "AFIAFT"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 440
+                    id2: 33
+                    name: "AFGGFXNI0"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 448
+                    id2: 34
+                    name: "AFCMCCNI0"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031645
+                    index: 0
+                    unk2: 456
+                    id2: 35
+                    name: "AMCC0_P0"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031645
+                    index: 0
+                    unk2: 464
+                    id2: 36
+                    name: "AMCC0_P1"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031645
+                    index: 0
+                    unk2: 472
+                    id2: 37
+                    name: "AMCC0_P2"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031645
+                    index: 0
+                    unk2: 480
+                    id2: 38
+                    name: "AMCC0_P3"
+                  }
+                  {
+                    alias: 2031645
+                    index: 0
+                    unk2: 488
+                    id2: 39
+                    name: "AFINS0"
+                  }
+                  {
+                    flag: 130
+                    id1: 5
+                    alias: 2031645
+                    index: 0
+                    unk2: 496
+                    id2: 40
+                    name: "GFX"
+                  }
+                  {
+                    flag: 9
+                    alias: 35
+                    index: 0
+                    unk2: 504
+                    id2: 41
+                    name: "DCS0"
+                  }
+                  {
+                    flag: 9
+                    alias: 36
+                    index: 0
+                    unk2: 512
+                    id2: 42
+                    name: "DCS1"
+                  }
+                  {
+                    flag: 9
+                    alias: 37
+                    index: 0
+                    unk2: 520
+                    id2: 43
+                    name: "DCS2"
+                  }
+                  {
+                    flag: 9
+                    alias: 38
+                    index: 0
+                    unk2: 528
+                    id2: 44
+                    name: "DCS3"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031655
+                    index: 0
+                    unk2: 536
+                    id2: 45
+                    name: "AFISOCNI0"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031655
+                    index: 0
+                    unk2: 544
+                    id2: 46
+                    name: "AFISOCNI1"
+                  }
+                  {
+                    flag: 9
+                    alias: 2031655
+                    index: 0
+                    unk2: 552
+                    id2: 47
+                    name: "AFISOCNI2"
+                  }
+                  {
+                    flag: 2
+                    id1: 15
+                    alias: 45
+                    index: 0
+                    unk2: 592
+                    id2: 52
+                    name: "PRORES"
+                  }
+                  {
+                    flag: 1
+                    alias: 46
+                    index: 0
+                    unk2: 600
+                    id2: 53
+                    name: "APCIE_GP"
+                  }
+                  {
+                    flag: 1
+                    alias: 46
+                    index: 0
+                    unk2: 608
+                    id2: 54
+                    name: "SIO"
+                  }
+                  {
+                    flag: 2
+                    id1: 12
+                    alias: 46
+                    index: 0
+                    unk2: 624
+                    id2: 56
+                    name: "AVD_SYS"
+                  }
                   {
-                    map: 7
+                    unk2: 16
-                    index: 2
+                    index: 0
-                    name: "ECPU2"
+                    name: "ECPU_2"
                   }
-                  {
-                    index: 21
-                    map: 8
-                    id2: 36
-                    name: "ATC0_USB_AON"
-                  }
+                  {
+                    flag: 1
+                    alias: 46
+                    index: 0
+                    unk2: 632
+                    id2: 57
+                    name: "ANS"
+                  }
+                  {
+                    flag: 2
+                    id1: 8
+                    alias: 47
+                    index: 0
+                    unk2: 640
+                    id2: 58
+                    name: "DISP_SYS"
+                  }
+                  {
+                    flag: 2
+                    id1: 9
+                    alias: 47
+                    index: 0
+                    unk2: 648
+                    id2: 59
+                    name: "DISPEXT0_SYS"
+                  }
+                  {
+                    flag: 128
+                    alias: 47
+                    index: 0
+                    unk2: 656
+                    id2: 60
+                    name: "ANE_SYS"
+                  }
+                  {
+                    flag: 1
+                    alias: 53
+                    index: 0
+                    unk2: 672
+                    id2: 62
+                    name: "APCIE_SYS_GP"
+                  }
+                  {
+                    flag: 1
+                    alias: 54
+                    index: 0
+                    unk2: 680
+                    id2: 63
+                    name: "SIO_CPU"
+                  }
+                  {
+                    flag: 1
+                    alias: 54
+                    index: 0
+                    unk2: 688
+                    id2: 64
+                    name: "FPWM0"
+                  }
+                  {
+                    flag: 1
+                    alias: 54
+                    index: 0
+                    unk2: 752
+                    id2: 72
+                    name: "SPI_P"
+                  }
+                  {
+                    flag: 9
+                    alias: 54
+                    index: 0
+                    unk2: 768
+                    id2: 74
+                    name: "DPA_P"
+                  }
+                  {
+                    flag: 1
+                    alias: 54
+                    index: 0
+                    unk2: 776
+                    id2: 75
+                    name: "AES"
+                  }
                   {
-                    map: 8
+                    unk2: 416
-                    index: 22
+                    index: 0
-                    id2: 37
+                    id2: 30
                   }
-                  {
-                    flag: 41
-                    alias: 33
-                    index: 23
-                    map: 8
-                    id2: 38
-                    name: "DCS2"
-                  }
-                  {
-                    flag: 41
-                    alias: 33
-                    index: 24
-                    map: 8
-                    id2: 39
-                    name: "DCS1"
-                  }
-                  {
-                    flag: 41
-                    alias: 33
-                    index: 25
-                    map: 8
-                    id2: 40
-                    name: "DCS3"
-                  }
-                  {
-                    flag: 41
-                    alias: 33
-                    index: 26
-                    map: 8
-                    id2: 41
-                    unk4: 21
-                    name: "SMX0"
-                  }
-                  {
-                    flag: 41
-                    alias: 41
-                    index: 27
-                    map: 8
-                    id2: 42
-                    unk4: 18
-                    name: "LMX0"
-                  }
-                  {
-                    flag: 34
-                    id1: 13
-                    alias: 42
-                    index: 28
-                    map: 8
-                    id2: 43
-                    unk4: 2
-                    name: "JPG"
-                  }
-                  {
-                    flag: 34
-                    id1: 12
-                    alias: 42
-                    index: 29
-                    map: 8
-                    id2: 44
-                    unk4: 1
-                    name: "MSR"
-                  }
-                  {
-                    flag: 34
-                    id1: 10
-                    alias: 42
-                    index: 30
-                    map: 8
-                    id2: 45
-                    unk4: 3
-                    name: "VENC_SYS"
-                  }
+                  {
+                    flag: 1
+                    alias: 57
+                    index: 0
+                    unk2: 784
+                    id2: 76
+                    name: "APCIE_ST"
+                  }
+                  {
+                    alias: 59
+                    index: 0
+                    unk2: 800
+                    id2: 78
+                    name: "DISPEXT0_FE"
+                  }
+                  {
+                    alias: 78
+                    index: 0
+                    unk1: 67108864
+                    unk2: 808
+                    id2: 79
+                    name: "DISPEXT0_CPU"
+                  }
+                  {
+                    alias: 72
+                    index: 0
+                    unk2: 816
+                    id2: 80
+                    name: "SPI0"
+                  }
+                  {
+                    alias: 72
+                    index: 0
+                    unk2: 832
+                    id2: 82
+                    name: "SPI2"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 856
+                    id2: 85
+                    name: "UART_N"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 864
+                    id2: 86
+                    name: "UART0"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 872
+                    id2: 87
+                    name: "UART1"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 880
+                    id2: 88
+                    name: "UART2"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 888
+                    id2: 89
+                    name: "UART3"
+                  }
+                  {
+                    flag: 1
+                    alias: 73
+                    index: 0
+                    unk2: 904
+                    id2: 91
+                    name: "UART5"
+                  }
+                  {
+                    alias: 74
+                    index: 0
+                    unk2: 912
+                    id2: 92
+                    name: "DPA0"
+                  }
+                  {
+                    alias: 74
+                    index: 0
+                    unk2: 920
+                    id2: 93
+                    name: "DPA1"
+                  }
+                  {
+                    flag: 1
+                    alias: 4980793
+                    index: 0
+                    unk2: 928
+                    id2: 94
+                    name: "APCIE_SYS_ST"
+                  }
+                  {
+                    flag: 16
+                    alias: 78
+                    index: 0
+                    unk2: 936
+                    id2: 95
+                    name: "DISPEXT0_DBE"
+                  }
+                  {
+                    flag: 16
+                    alias: 78
+                    index: 0
+                    unk2: 944
+                    id2: 96
+                    name: "DPEXT0"
+                  }
+                  {
+                    flag: 16
+                    alias: 78
+                    index: 0
+                    unk2: 952
+                    id2: 97
+                    name: "DISPEXT0_GPPP"
+                  }
+                  {
+                    flag: 1
+                    alias: 4063326
+                    index: 0
+                    unk2: 960
+                    id2: 98
+                    name: "APCIE_PHY_SW"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 968
+                    id2: 99
+                    name: "DPTX_PHY"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 976
+                    id2: 100
+                    name: "PMP"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 984
+                    id2: 101
+                    name: "PMS_SRAM"
+                  }
+                  {
+                    index: 0
+                    unk2: 992
+                    id2: 102
+                    name: "ATC0_USB_AON"
+                  }
+                  {
+                    alias: 6684719
+                    index: 0
+                    unk2: 1000
+                    id2: 103
+                    name: "ATC0_COMMON"
+                  }
+                  {
+                    alias: 106
+                    index: 0
+                    unk2: 16392
+                    id2: 107
+                    name: "ISP_CPU_CORE0"
+                  }
+                  {
+                    alias: 106
+                    index: 0
+                    unk2: 16400
+                    id2: 108
+                    name: "ISP_CPU_CORE1"
+                  }
+                  {
+                    alias: 55
+                    index: 0
+                    unk2: 16408
+                    id2: 109
+                    name: "ISP_FE"
+                  }
+                  {
+                    alias: 109
+                    index: 0
+                    unk2: 16432
+                    id2: 112
+                    name: "ISP_STS0"
+                  }
+                  {
+                    alias: 109
+                    index: 0
+                    unk2: 16440
+                    id2: 113
+                    name: "ISP_STS1"
+                  }
+                  {
+                    alias: 109
+                    index: 0
+                    unk2: 16448
+                    id2: 114
+                    name: "ISP_PEARL"
+                  }
+                  {
+                    alias: 109
+                    index: 0
+                    unk2: 16456
+                    id2: 115
+                    name: "ISP_BE"
+                  }
+                  {
+                    alias: 115
+                    index: 0
+                    unk2: 16464
+                    id2: 116
+                    name: "ISP_CLR"
+                  }
+                  {
+                    alias: 115
+                    index: 0
+                    unk2: 16472
+                    id2: 117
+                    name: "ISP_CVD"
+                  }
+                  {
+                    alias: 50
+                    index: 0
+                    unk2: 32768
+                    id2: 119
+                    name: "VENC0_DMA"
+                  }
+                  {
+                    alias: 124
+                    index: 0
+                    unk2: 32824
+                    id2: 126
+                    name: "VENC1_PIPE5"
+                  }
+                  {
+                    alias: 124
+                    index: 0
+                    unk2: 32832
+                    id2: 127
+                    name: "VENC1_ME0"
+                  }
+                  {
+                    alias: 127
+                    index: 0
+                    unk2: 32840
+                    id2: 128
+                    name: "VENC1_ME1"
+                  }
+                  {
+                    flag: 16
+                    alias: 60
+                    index: 0
+                    unk2: 49152
+                    id2: 129
+                    name: "ANE_CPU"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65544
+                    id2: 133
+                    name: "DISP_GP0"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65552
+                    id2: 134
+                    name: "DISP_GP1"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65560
+                    id2: 135
+                    name: "DISP_CMB"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65568
+                    id2: 136
+                    name: "DISP_PPP"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65576
+                    id2: 137
+                    name: "DISP_HILO"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65584
+                    id2: 138
+                    name: "DISP_DBE"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65592
+                    id2: 139
+                    name: "DP"
+                  }
+                  {
+                    flag: 16
+                    alias: 77
+                    index: 0
+                    unk2: 65600
+                    id2: 140
+                    name: "MIPI_DSI"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777304
+                    id2: 142
+                    name: "NUB_SPMI0"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777312
+                    id2: 143
+                    name: "NUB_SPMI1"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777320
+                    id2: 144
+                    name: "NUB_SPMI_A0"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777328
+                    id2: 145
+                    name: "NUB_AON"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777336
+                    id2: 146
+                    name: "NUB_AON_NOGATE"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16777360
+                    id2: 149
+                    name: "DSG"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16777368
+                    id2: 150
+                    name: "HPD"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777376
+                    id2: 151
+                    name: "NUB_FABRIC"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777384
+                    id2: 152
+                    name: "NUB_SRAM"
+                  }
+                  {
+                    flag: 9
+                    index: 0
+                    unk2: 16777392
+                    id2: 153
+                    name: "DEBUG_SWITCH"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16793600
+                    id2: 154
+                    name: "AOP_FILTER"
+                  }
+                  {
+                    flag: 16
+                    alias: 154
+                    index: 0
+                    unk2: 16793608
+                    id2: 155
+                    name: "AOP_GPIO"
+                  }
+                  {
+                    flag: 16
+                    alias: 154
+                    index: 0
+                    unk2: 16793616
+                    id2: 156
+                    name: "AOP_BASE"
+                  }
+                  {
+                    flag: 16
+                    alias: 154
+                    index: 0
+                    unk2: 16793624
+                    id2: 157
+                    name: "AOP_FR"
+                  }
+                  {
+                    flag: 16
+                    alias: 154
+                    index: 0
+                    unk2: 16793632
+                    id2: 158
+                    name: "AUDIO_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 156
+                    index: 0
+                    unk2: 16793640
+                    id2: 159
+                    name: "AOP_SHIM"
+                  }
+                  {
+                    flag: 16
+                    alias: 156
+                    index: 0
+                    unk2: 16793648
+                    id2: 160
+                    name: "AOP_PIODMA"
+                  }
+                  {
+                    flag: 16
+                    alias: 156
+                    index: 0
+                    unk2: 16793656
+                    id2: 161
+                    name: "AOP2_PIODMA"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793664
+                    id2: 162
+                    name: "AOP_I2CM0"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793672
+                    id2: 163
+                    name: "AOP_I2CM1"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793680
+                    id2: 164
+                    name: "AOP_I2CM2"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793688
+                    id2: 165
+                    name: "AOP_I2CM3"
+                  }
+                  {
+                    flag: 16
+                    alias: 10289308
+                    index: 0
+                    unk2: 16793696
+                    id2: 166
+                    name: "AOP_SCM"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793704
+                    id2: 167
+                    name: "AOP_SPI0"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793712
+                    id2: 168
+                    name: "AOP_SPI1"
+                  }
+                  {
+                    flag: 16
+                    alias: 10289306
+                    index: 0
+                    unk2: 16793720
+                    id2: 169
+                    name: "AOP_SPMI0"
+                  }
+                  {
+                    flag: 16
+                    alias: 10289306
+                    index: 0
+                    unk2: 16793728
+                    id2: 170
+                    name: "AOP_SPMI1"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793736
+                    id2: 171
+                    name: "AOP_HE_NRCS0"
+                  }
+                  {
+                    flag: 16
+                    alias: 157
+                    index: 0
+                    unk2: 16793744
+                    id2: 172
+                    name: "AOP_HE_NRCS1"
+                  }
+                  {
+                    flag: 16
+                    alias: 10289308
+                    index: 0
+                    unk2: 16793752
+                    id2: 173
+                    name: "AOP_CPU"
+                  }
+                  {
+                    flag: 16
+                    alias: 10289308
+                    index: 0
+                    unk2: 16793760
+                    id2: 174
+                    name: "AOP2_CPU"
+                  }
+                  {
+                    flag: 16
+                    alias: 158
+                    index: 0
+                    unk2: 16793768
+                    id2: 175
+                    name: "AUDIO_FR"
+                  }
+                  {
+                    flag: 16
+                    alias: 159
+                    index: 0
+                    unk2: 16793776
+                    id2: 176
+                    name: "AOP_UART0"
+                  }
+                  {
+                    flag: 16
+                    alias: 159
+                    index: 0
+                    unk2: 16793784
+                    id2: 177
+                    name: "AOP_UART1"
+                  }
+                  {
+                    flag: 16
+                    alias: 159
+                    index: 0
+                    unk2: 16793792
+                    id2: 178
+                    name: "AOP_UART2"
+                  }
+                  {
+                    flag: 16
+                    alias: 11337894
+                    index: 0
+                    unk2: 16793800
+                    id2: 179
+                    name: "AOP_SRAM"
+                  }
+                  {
+                    flag: 16
+                    alias: 175
+                    index: 0
+                    unk2: 16793808
+                    id2: 180
+                    name: "AUDIO_P"
+                  }
+                  {
+                    flag: 16
+                    alias: 175
+                    index: 0
+                    unk2: 16793816
+                    id2: 181
+                    name: "AUDIO_LEAP_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 175
+                    index: 0
+                    unk2: 16793824
+                    id2: 182
+                    name: "AUDIO_SENSE_PDMC"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793832
+                    id2: 183
+                    name: "AUDIO_BASE_S_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793840
+                    id2: 184
+                    name: "AUDIO_BASE_NS_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793848
+                    id2: 185
+                    name: "AUDIO_LEAP_MCA"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793856
+                    id2: 186
+                    name: "AUDIO_MCA0_M"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793864
+                    id2: 187
+                    name: "AUDIO_MCA1_M"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793872
+                    id2: 188
+                    name: "AUDIO_MCA2_M"
+                  }
                   {
-                    map: 7
+                    unk2: 24
-                    index: 3
+                    index: 0
-                    name: "ECPU3"
+                    name: "ECPU_3"
                   }
-                  {
-                    flag: 34
-                    id1: 11
-                    alias: 42
-                    index: 31
-                    map: 8
-                    id2: 46
-                    unk4: 4
-                    name: "AVD_SYS"
-                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793880
+                    id2: 189
+                    name: "AUDIO_MCA3_M"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793888
+                    id2: 190
+                    name: "AUDIO_MCA4_M"
+                  }
+                  {
+                    flag: 16
+                    alias: 180
+                    index: 0
+                    unk2: 16793896
+                    id2: 191
+                    name: "AUDIO_MCA5_M"
+                  }
+                  {
+                    flag: 16
+                    alias: 181
+                    index: 0
+                    unk2: 16793904
+                    id2: 192
+                    name: "AUDIO_LEAP_C"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793912
+                    id2: 193
+                    name: "AUDIO_LEAP_S_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793920
+                    id2: 194
+                    name: "AUDIO_LEAP_NS_A"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793928
+                    id2: 195
+                    name: "AUDIO_LEAP_RX0"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793936
+                    id2: 196
+                    name: "AUDIO_LEAP_RX1"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793944
+                    id2: 197
+                    name: "AUDIO_LEAP_RX2"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793952
+                    id2: 198
+                    name: "AUDIO_LEAP_RX3"
+                  }
                   {
-                    map: 9
-                    unk4: 14
+                    unk2: 560
-                    alias: 42
+                    alias: 45
-                    id2: 47
+                    id2: 48
-                    name: "PRORES"
+                    name: "JPG"
                   }
-                  {
-                    alias: 44
-                    index: 1
-                    map: 9
-                    id2: 48
-                    name: "MSR_ASE_CORE"
-                  }
-                  {
-                    flag: 41
-                    alias: 41
-                    index: 2
-                    map: 9
-                    id2: 49
-                    unk4: 19
-                    name: "LMX1"
-                  }
-                  {
-                    flag: 1
-                    alias: 49
-                    index: 3
-                    map: 9
-                    id2: 50
-                    name: "APCIE"
-                  }
-                  {
-                    flag: 41
-                    alias: 49
-                    index: 4
-                    map: 9
-                    id2: 51
-                    unk4: 16
-                    name: "SIO"
-                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793960
+                    id2: 199
+                    name: "AUDIO_LEAP_RX4"
+                  }
+                  {
+                    flag: 16
+                    alias: 192
+                    index: 0
+                    unk2: 16793968
+                    id2: 200
+                    name: "AUDIO_LEAP_TX0"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16793976
+                    id2: 201
+                    name: "PDM0_AUDIO_REF"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16793984
+                    id2: 202
+                    name: "PDM1_AUDIO_REF"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    unk2: 16809984
+                    id2: 203
+                    name: "SMC_FABRIC"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16809992
+                    id2: 204
+                    name: "SMC_GPIO"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810000
+                    id2: 205
+                    name: "SMC_AON"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810008
+                    id2: 206
+                    name: "SMC_UART0"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810016
+                    id2: 207
+                    name: "SMC_UART1"
+                  }
+                  {
+                    flag: 1
+                    alias: 203
+                    index: 0
+                    unk2: 16810024
+                    id2: 208
+                    name: "SMC_I2CM0"
+                  }
+                  {
+                    flag: 1
+                    alias: 203
+                    index: 0
+                    unk2: 16810032
+                    id2: 209
+                    name: "SMC_I2CM1"
+                  }
+                  {
+                    flag: 1
+                    alias: 203
+                    index: 0
+                    unk2: 16810040
+                    id2: 210
+                    name: "SMC_I2CM2"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810048
+                    id2: 211
+                    name: "SMC_FPWM0"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810056
+                    id2: 212
+                    name: "SMC_FPWM1"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810064
+                    id2: 213
+                    name: "SMC_FPWM2"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810072
+                    id2: 214
+                    name: "SMC_FPWM3"
+                  }
+                  {
+                    flag: 16
+                    alias: 9502923
+                    index: 0
+                    unk2: 16810080
+                    id2: 215
+                    name: "SMC_PTD"
+                  }
+                  {
+                    flag: 16
+                    alias: 203
+                    index: 0
+                    unk2: 16810088
+                    id2: 216
+                    name: "SMC_CPU"
+                  }
+                  {
+                    flag: 16
+                    alias: 9306327
+                    index: 0
+                    unk2: 16810096
+                    id2: 217
+                    name: "NUB_HE_NRCS0"
+                  }
+                  {
+                    flag: 16
+                    alias: 9371863
+                    index: 0
+                    unk2: 16810104
+                    id2: 218
+                    name: "NUB_HE_NRCS1"
+                  }
+                  {
+                    flag: 16
+                    alias: 151
+                    index: 0
+                    unk2: 16826368
+                    id2: 219
+                    name: "MTP_FABRIC"
+                  }
+                  {
+                    flag: 16
+                    alias: 219
+                    index: 0
+                    unk2: 16826376
+                    id2: 220
+                    name: "MTP_GPIO"
+                  }
+                  {
+                    flag: 16
+                    alias: 219
+                    index: 0
+                    unk2: 16826384
+                    id2: 221
+                    name: "MTP_BASE"
+                  }
+                  {
+                    flag: 16
+                    alias: 219
+                    index: 0
+                    unk2: 16826392
+                    id2: 222
+                    name: "MTP_PERIPH"
+                  }
+                  {
+                    flag: 16
+                    alias: 219
+                    index: 0
+                    unk2: 16826400
+                    id2: 223
+                    name: "MTP_UART0"
+                  }
+                  {
+                    flag: 16
+                    alias: 219
+                    index: 0
+                    unk2: 16826408
+                    id2: 224
+                    name: "MTP_CPU"
+                  }
+                  {
+                    flag: 16
+                    alias: 222
+                    index: 0
+                    unk2: 16826416
+                    id2: 225
+                    name: "MTP_SCM_FABRIC"
+                  }
+                  {
+                    flag: 16
+                    alias: 222
+                    index: 0
+                    unk2: 16826424
+                    id2: 226
+                    name: "MTP_SPI0"
+                  }
+                  {
+                    flag: 16
+                    alias: 222
+                    index: 0
+                    unk2: 16826432
+                    id2: 227
+                    name: "MTP_I2CM0"
+                  }
+                  {
+                    flag: 16
+                    alias: 14680289
+                    index: 0
+                    unk2: 16826440
+                    id2: 228
+                    name: "MTP_SRAM"
+                  }
+                  {
+                    flag: 16
+                    alias: 228
+                    index: 0
+                    unk2: 16826448
+                    id2: 229
+                    name: "MTP_DMA"
+                  }
+                  {
+                    flag: 16
+                    alias: 40
+                    index: 0
+                    id2: 321
+                    name: "GFX-ASC1"
+                  }
+                  {
+                    flag: 18
+                    id1: 10
+                    index: 0
+                    id2: 249
+                    name: "VENC0-AVE-VMAX"
+                  }
+                  {
+                    flag: 18
+                    id1: 12
+                    index: 0
+                    id2: 251
+                    name: "AVD-SOC-VMAX"
+                  }
+                  {
+                    flag: 18
+                    id1: 14
+                    index: 0
+                    id2: 253
+                    name: "JPG-SOC-VMAX"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 256
+                    name: "CLPC-SOC-VNOM"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 257
+                    name: "CLPC-SOC-VMAX"
+                  }
+                  {
+                    flag: 18
+                    id1: 15
+                    index: 0
+                    id2: 261
+                    name: "PRORES-SOC-VMAX"
+                  }
+                  {
+                    flag: 18
+                    id1: 13
+                    index: 0
+                    id2: 263
+                    name: "MSR-SOC-VMAX"
+                  }
+                  {
+                    flag: 18
+                    id1: 11
+                    index: 0
+                    id2: 264
+                    name: "VENC1-AVE-VNOM"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 265
+                    name: "VENC1-MEM-FAST"
+                  }
+                  {
+                    flag: 18
+                    id1: 11
+                    index: 0
+                    id2: 266
+                    name: "VENC1-AVE-VMAX"
+                  }
+                  {
+                    flag: 16
+                    alias: 50
+                    index: 0
+                    id2: 306
+                    name: "VENC0-SYS-V"
+                  }
+                  {
+                    flag: 16
+                    alias: 51
+                    index: 0
+                    id2: 307
+                    name: "VENC1-SYS-V"
+                  }
+                  {
+                    flag: 18
+                    id1: 28
+                    index: 0
+                    unk1: 2147483648
+                    id2: 296
+                    name: "SEP-PEARL-V"
+                  }
+                  {
+                    flag: 16
+                    alias: 94
+                    index: 0
+                    id2: 308
+                    name: "APCIE_SYS_ST-V"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 322
+                    name: "VENC-CLSTR-V"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 336
+                    name: "DISP_INT_M3"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 337
+                    name: "DISP_EXT0_M3"
+                  }
+                  {
+                    flag: 18
+                    id1: 6
+                    index: 0
+                    unk1: 2147483648
+                    id2: 338
+                    name: "ANE-SYS-V-PMP"
+                  }
                   {
-                    map: 9
-                    unk4: 6
+                    unk2: 616
-                    alias: 49
+                    alias: 46
-                    index: 5
+                    index: 0
-                    id2: 52
+                    id2: 55
                   }
-                  {
-                    flag: 33
-                    alias: 49
-                    index: 6
-                    map: 9
-                    id2: 53
-                    unk4: 13
-                    name: "ANS"
-                  }
-                  {
-                    flag: 33
-                    alias: 50
-                    index: 7
-                    map: 9
-                    id2: 54
-                    unk4: 9
-                    name: "APCIE_GP"
-                  }
-                  {
-                    flag: 33
-                    alias: 51
-                    index: 8
-                    map: 9
-                    id2: 55
-                    name: "SIO_CPU"
-                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 339
+                    name: "ATC0-DCS-F1"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 340
+                    name: "ATC0-DCS-F2"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 341
+                    name: "ATC0-DCS-F3"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 342
+                    name: "ATC0-DCS-F4"
+                  }
+                  {
+                    flag: 16
+                    index: 0
+                    id2: 343
+                    name: "ATC0-DCS-F5"
+                  }
                   {
-                    map: 7
+                    unk2: 48
-                    index: 4
+                    index: 0
-                    name: "PCPU0"
+                    name: "PCPU_0"
                   }
-                  {
-                    flag: 1
-                    alias: 51
-                    index: 9
-                    map: 9
-                    id2: 56
-                    name: "FPWM0"
-                  }
-                  {
-                    alias: 51
-                    index: 10
-                    map: 9
-                    id2: 57
-                    name: "FPWM1"
-                  }
-                  {
-                    alias: 51
-                    index: 11
-                    map: 9
-                    id2: 58
-                    name: "FPWM2"
-                  }
                   {
-                    map: 9
+                    unk2: 712
-                    alias: 51
+                    alias: 54
-                    index: 12
+                    index: 0
-                    id2: 59
+                    id2: 67
                   }
                   {
-                    map: 9
+                    unk2: 720
-                    alias: 51
+                    alias: 54
-                    index: 13
+                    index: 0
-                    id2: 60
+                    id2: 68
                   }
                   {
-                    map: 9
+                    unk2: 664
-                    alias: 51
+                    alias: 49
-                    index: 14
+                    index: 0
-                    name: "I2C2"
+                    name: "MSR_ASE_CORE"
                   }
-                  {
-                    alias: 51
-                    index: 15
-                    map: 9
-                    id2: 62
-                    name: "I2C3"
-                  }
-                  {
-                    alias: 51
-                    index: 16
-                    map: 9
-                    id2: 63
-                    name: "I2C4"
-                  }
-                  {
-                    flag: 1
-                    alias: 51
-                    index: 17
-                    map: 9
-                    id2: 64
-                    name: "SPI_P"
-                  }
                   {
-                    map: 9
+                    unk2: 696
-                    alias: 51
+                    alias: 54
-                    index: 18
+                    index: 0
-                    name: "UART_P"
+                    name: "FPWM1"
                   }
                   {
-                    map: 7
+                    unk2: 56
-                    index: 5
+                    index: 0
-                    name: "PCPU1"
+                    name: "PCPU_1"
                   }
                   {
-                    map: 9
+                    unk2: 704
-                    alias: 51
+                    alias: 54
-                    index: 19
+                    index: 0
-                    name: "AUDIO_P"
+                    name: "FPWM2"
                   }
-                  {
-                    flag: 1
-                    alias: 51
-                    index: 20
-                    map: 9
-                    id2: 67
-                    name: "AES"
-                  }
-                  {
-                    flag: 33
-                    alias: 3473458
-                    index: 21
-                    map: 9
-                    id2: 68
-                    name: "APCIE_ST"
-                  }
                   {
-                    map: 9
+                    unk2: 728
-                    alias: 64
+                    alias: 54
-                    index: 22
+                    index: 0
-                    name: "SPI0"
+                    name: "I2C2"
                   }
                   {
-                    map: 9
+                    unk2: 736
-                    alias: 64
+                    alias: 54
-                    index: 23
+                    index: 0
-                    name: "SPI1"
+                    name: "I2C3"
                   }
                   {
-                    map: 9
+                    unk2: 744
-                    alias: 64
+                    alias: 54
-                    index: 24
+                    index: 0
-                    name: "SPI2"
+                    name: "I2C4"
                   }
-                  {
-                    alias: 64
-                    index: 25
-                    map: 9
-                    id2: 72
-                    name: "SPI3"
-                  }
                   {
-                    map: 9
+                    unk2: 760
-                    alias: 64
+                    alias: 54
-                    index: 26
+                    index: 0
-                    name: "QSPI"
+                    name: "UART_P"
                   }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 27
-                    map: 9
-                    id2: 74
-                    name: "UART_N"
-                  }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 28
-                    map: 9
-                    id2: 75
-                    name: "UART0"
-                  }
                   {
-                    map: 7
+                    unk2: 80
-                    index: 8
+                    index: 0
                   }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 29
-                    map: 9
-                    id2: 76
-                    name: "UART1"
-                  }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 30
-                    map: 9
-                    id2: 77
-                    name: "UART2"
-                  }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 31
-                    map: 9
-                    id2: 78
-                    name: "UART3"
-                  }
                   {
-                    map: 10
+                    unk2: 896
-                    alias: 65
+                    alias: 73
-                    id2: 79
+                    id2: 90
                   }
-                  {
-                    flag: 1
-                    alias: 65
-                    index: 1
-                    map: 10
-                    id2: 80
-                    name: "UART5"
-                  }
                   {
-                    map: 10
+                    unk2: 824
-                    alias: 66
+                    alias: 72
-                    index: 2
+                    index: 0
-                    name: "SIO_ADMA"
+                    name: "SPI1"
                   }
-                  {
-                    flag: 16
-                    index: 3
-                    map: 10
-                    id2: 82
-                    name: "DPTX_PHY"
-                  }
                   {
-                    map: 10
+                    unk2: 840
-                    alias: 66
+                    alias: 72
-                    index: 4
+                    index: 0
-                    name: "DPA0"
+                    name: "SPI3"
                   }
                   {
-                    map: 10
+                    unk2: 848
-                    alias: 66
+                    alias: 72
-                    index: 5
+                    index: 0
-                    name: "DPA1"
+                    name: "QSPI"
                   }
-                  {
-                    flag: 33
-                    alias: 4456502
-                    index: 6
-                    map: 10
-                    id2: 85
-                    name: "APCIE_PHY_SW"
-                  }
                   {
-                    map: 7
+                    unk2: 88
-                    index: 9
+                    index: 0
                   }
-                  {
-                    alias: 4325457
-                    index: 7
-                    map: 10
-                    id2: 86
-                    name: "MCA0"
-                  }
-                  {
-                    alias: 4325457
-                    index: 8
-                    map: 10
-                    id2: 87
-                    name: "MCA1"
-                  }
-                  {
-                    alias: 4325457
-                    index: 9
-                    map: 10
-                    id2: 88
-                    name: "MCA2"
-                  }
-                  {
-                    alias: 4325457
-                    index: 10
-                    map: 10
-                    id2: 89
-                    name: "MCA3"
-                  }
-                  {
-                    flag: 41
-                    alias: 41
-                    index: 11
-                    map: 10
-                    id2: 90
-                    unk4: 20
-                    name: "LMX2"
-                  }
-                  {
-                    flag: 66
-                    id1: 8
-                    alias: 90
-                    index: 12
-                    map: 10
-                    id2: 91
-                    unk4: 7
-                    name: "DISP_SYS"
-                  }
-                  {
-                    flag: 66
-                    id1: 9
-                    alias: 90
-                    index: 13
-                    map: 10
-                    id2: 92
-                    unk4: 11
-                    name: "DISPEXT_SYS"
-                  }
-                  {
-                    flag: 162
-                    id1: 6
-                    alias: 90
-                    index: 14
-                    map: 10
-                    unk1: 1900544
-                    id2: 93
-                    unk4: 5
-                    name: "ANE_SYS"
-                  }
-                  {
-                    flag: 41
-                    index: 15
-                    map: 10
-                    id2: 94
-                    name: "PMP"
-                  }
-                  {
-                    flag: 41
-                    index: 16
-                    map: 10
-                    id2: 95
-                    name: "PMS_SRAM"
-                  }
-                  {
-                    flag: 41
-                    index: 0
-                    map: 8
-                    id2: 15
-                    unk4: 12
-                    name: "SBR"
-                  }
                   {
-                    map: 10
+                    unk2: 792
-                    alias: 91
+                    alias: 58
-                    index: 17
+                    index: 0
-                    id2: 96
+                    id2: 77
                   }
-                  {
-                    alias: 92
-                    index: 18
-                    map: 10
-                    id2: 97
-                    name: "DISPEXT_FE"
-                  }
-                  {
-                    flag: 162
-                    id1: 5
-                    index: 19
-                    map: 10
-                    id2: 98
-                    unk4: 8
-                    name: "GFX"
-                  }
-                  {
-                    flag: 32
-                    alias: 97
-                    index: 20
-                    map: 10
-                    unk1: 1114112
-                    id2: 99
-                    name: "DISPEXT_CPU"
-                  }
-                  {
-                    flag: 16
-                    alias: 97
-                    index: 21
-                    map: 10
-                    id2: 100
-                    name: "DISPEXT_BE"
-                  }
-                  {
-                    flag: 48
-                    alias: 97
-                    index: 22
-                    map: 10
-                    id2: 101
-                    name: "DISPEXT_GP0"
-                  }
-                  {
-                    flag: 48
-                    alias: 97
-                    index: 23
-                    map: 10
-                    id2: 102
-                    name: "DISPEXT_GP1"
-                  }
-                  {
-                    alias: 5898276
-                    index: 24
-                    map: 10
-                    id2: 103
-                    unk4: 10
-                    name: "ATC0_COMMON"
-                  }
                   {
-                    map: 10
+                    unk2: 1008
-                    alias: 2359399
+                    alias: 103
-                    index: 25
+                    index: 0
                   }
-                  {
-                    flag: 48
-                    alias: 97
-                    index: 26
-                    map: 10
-                    id2: 105
-                    name: "DISPEXT_PPP"
-                  }
                 ]
-                energy-counters: "AAADBQAAABVFQ1BVMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwYAAAAVRUNQVTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMHAAAAFUVDUFUyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCAAAABVFQ1BVMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwkAAAAWUENQVTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMKAAAAFlBDUFUxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECwAAABVFQ1BNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAwAAAAWUENQTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAUNAAAAFUVDUFUwX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAFDgAAABVFQ1BVMV9TUkFNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMABQ8AAAAVRUNQVTJfU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAUQAAAAFUVDUFUzX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAFEQAAABZQQ1BVMF9TUkFNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYABRIAAAAWUENQVTFfU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAABRAQYTAAAAFUVDUE1fU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUgEGFAAAABZQQ1BNX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhUAAAAXRUNQVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIWAAAAF1BDUFUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACFwAAAABDUFUgRW5lcmd5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
+                energy-counters: "AAADBQAAABVFQ1BVMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwYAAAAVRUNQVTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMHAAAAFUVDUFUyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCAAAABVFQ1BVMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwkAAAAWUENQVTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMKAAAAFlBDUFUxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECwAAABVFQ1BNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAwAAAAWUENQTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAUNAAAAFUVDUFUwX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAFDgAAABVFQ1BVMV9TUkFNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMABQ8AAAAVRUNQVTJfU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAUQAAAAFUVDUFUzX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAFEQAAABZQQ1BVMF9TUkFNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYABRIAAAAWUENQVTFfU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAADnAAYTAAAAFUVDUE1fU1JBTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6AAGFAAAABZQQ1BNX1NSQU0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhUAAAAXRUNQVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIWAAAAF1BDUFUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACFwAAAABDUFUgRW5lcmd5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
                 function-mcc_ctrl: [
                   ...
-                  ")"
+                  "("
                 ]
                 function-pmp_control: [
                   ...
-                  "\\"
+                  "X"
                 ]
-                hw-dpe-reg: "AIDkEAIAAAAoAAAAAAAAAAAAAQAAAQBARUNQTQAAAAAAAAAAAAAAAACA5BECAAAAKAAAAAAAAAAAAAEAAAEAQFBDUE0AAAAAAAAAAAAAAAAAkAUQAgAAACgAAAAAAAAAAAABAAABAEBFQ09SRTAAAAAAAAAAAAAAAJAVEAIAAAAoAAAAAAAAAAAAAQAAAQBARUNPUkUxAAAAAAAAAAAAAACQJRACAAAAKAAAAAAAAAAAAAEAAAEAQEVDT1JFMgAAAAAAAAAAAAAAkDUQAgAAACgAAAAAAAAAAAABAAABAEBFQ09SRTMAAAAAAAAAAAAAAJAFEQIAAAAoAAAAAAAAAAAAAQAAAQBAUENPUkUwAAAAAAAAAAAAAACQFRECAAAAKAAAAAAAAAAAAAEAAAEAQFBDT1JFMQAAAAAAAAAAAAAJAAAAqQAAAIABAABAOAAAYgABAQEBAEBHUFUAAAAAAAAAAAAAAAAACQAAAKoAAACAAQAAQAIAAGIAAQEBAQBAR1BVIFNSQU0AAAAAAAAAAOBAkREDAAAACT0AANBKAABdAAEAAAABQEFORQAAAAAAAAAAAAAAAAAAgiDQAgAAAPoAAAA6DwAAHQABAAEBAUBJU1AAAAAAAAAAAAAAAAAACK8g0AIAAAD6AAAA9gMAAB0AAQABAQFAQVZFAAAAAAAAAAAAAAAAAAizINACAAAA+gAAAB4GAAAdAAEAAQEBQE1TUgAAAAAAAAAAAAAAAAAItyDQAgAAAPoAAAAaBQAAHQABAAEBAUBEQ1MAAAAAAAAAAAAAAAAACLsg0AIAAAD6AAAAigoAAB0AAQABAQFARFJBTQAAAAAAAAAAAAAAAAi/INACAAAA+gAAAFwEAAAdAAEAAQEBQERJU1AAAAAAAAAAAAAAAAAIwyDQAgAAAPoAAACOAgAAHQABAAEBAUBESVNQRVhUAAAAAAAAAAAA"
+                hw-dpe-reg: "AIDkEAIAAAAoAAAAAAAAAAAAAQAAAQBARUNQTQAAAAAAAAAAAAAAAACA5BECAAAAKAAAAAAAAAAAAAEAAAEAQFBDUE0AAAAAAAAAAAAAAAAAkAUQAgAAACgAAAAAAAAAAAABAAABAEBFQ09SRTAAAAAAAAAAAAAAAJAVEAIAAAAoAAAAAAAAAAAAAQAAAQBARUNPUkUxAAAAAAAAAAAAAACQJRACAAAAKAAAAAAAAAAAAAEAAAEAQEVDT1JFMgAAAAAAAAAAAAAAkDUQAgAAACgAAAAAAAAAAAABAAABAEBFQ09SRTMAAAAAAAAAAAAAAJAFEQIAAAAoAAAAAAAAAAAAAQAAAQBAUENPUkUwAAAAAAAAAAAAAACQFRECAAAAKAAAAAAAAAAAAAEAAAEAQFBDT1JFMQAAAAAAAAAAAAAJAAAAKQEAAIABAABAOAAAKAABAQEBAEBHUFUAAAAAAAAAAAAAAAAACQAAACoBAACAAQAAQAIAACgAAQEBAQBAR1BVIFNSQU0AAAAAAAAAAOCAlwEEAAAACT0AAJhSAAA8AAEAAAABQEFORQAAAAAAAAAAAAAAAAAIpyAAAwAAAPoAAADlDQAAGQABAAEBAUBJU1AAAAAAAAAAAAAAAAAACK8gAAMAAAD6AAAAbAYAABkAAQABAQFAQVZFAAAAAAAAAAAAAAAAAAi3IAADAAAA+gAAAAkFAAAZAAEAAQEBQE1TUgAAAAAAAAAAAAAAAAAIuyAAAwAAAPoAAABwFwAAGQABAAEBAUBBTUNDAAAAAAAAAAAAAAAACL8gAAMAAAD6AAAAAAAAABkAAQABAQFARENTAAAAAAAAAAAAAAAAAAjDIAADAAAA+gAAAGAMAAAZAAEAAQEBQERSQU0AAAAAAAAAAAAAAAAIxyAAAwAAAPoAAADwAwAAGQABAAEBAUBESVNQAAAAAAAAAAAAAAAACMsgAAMAAAD6AAAAAAAAABkAAQABAQFARElTUEVYVAAAAAAAAAAAAA=="
-                interrupt-config: "AAAAAVBNUF9TVEFUVVMAAAAAAAA="
+                interrupt-config: "AAAAAVBNUF9TVEFUVVMAAAAAAAABAAACQVZFX1BXUlVQAAAAAAAAAA=="
-                interrupts: 709
+                interrupts: 858993460039
-                panic-debug-switch-pg-wa: 20
+                panic-debug-switch-pg-wa: 153
-                panic-nub-pg-wa: 18
+                panic-nub-pg-wa: 151
                 reg: [
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
                   {
-                    addr: 3559391232
+                    addr: 4163371008
                   }
                   ...
                   ...
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
                   {
-                    addr: 3228712960
+                    addr: 4034019328
                   }
                   {
-                    addr: 3228729344
+                    addr: 4034035712
                   }
                   {
-                    addr: 3228762112
+                    addr: 4034068480
                   }
                   {
-                    addr: 3228958720
+                    addr: 4034265088
                   }
                   {
-                    addr: 3228975104
+                    addr: 4034281472
                   }
                   {
-                    addr: 3228991488
+                    addr: 4034297856
                   }
                   {
-                    addr: 3229089792
+                    addr: 4034396160
                   }
                   {
-                    addr: 3221225472
+                    addr: 4026531840
                   }
                   {
-                    addr: 3559620608
+                    addr: 4163600384
                   }
                   {
-                    addr: 3559686144
+                    addr: 4163665920
                   }
                   {
-                    addr: 3559718912
+                    addr: 4163698688
                   }
                   {
-                    addr: 3223355392
+                    addr: 4028661760
                   }
                   {
-                    addr: 3223846912
+                    addr: 4029153280
                   }
                   {
-                    addr: 3225157632
+                    addr: 4030464000
                   }
                   {
-                    addr: 3557818368
+                    addr: 4161798144
                   }
                   {
-                    addr: 4320559104
+                    addr: 8347156480
                   }
                   {
-                    addr: 3229089792
+                    addr: 4034396160
                   }
                   {
-                    addr: 4321148928
+                    addr: 8348090368
                   }
                   {
-                    addr: 3558866944
+                    addr: 4162846720
                   }
                   {
-                    addr: 4321165312
+                    addr: 8348106752
                   }
                   {
-                    addr: 4321247232
+                    addr: 8348188672
                   }
                   {
-                    size: 16203776
+                    size: 16728064
                   }
-                  {
-                    addr: 4496293888
-                    size: 16777216
-                  }
                   {
-                    addr: 2348810240
+                    addr: 4060086272
                   }
-                  {
-                    addr: 4362076160
-                    size: 16777216
-                  }
-                  {
-                    addr: 2013265920
-                    size: 16777216
-                  }
-                  {
-                    addr: 4294967296
-                    size: 16777216
-                  }
-                  {
-                    addr: 2281701376
-                    size: 16777216
-                  }
-                  {
-                    addr: 2130706432
-                    size: 16777216
-                  }
                   {
-                    addr: 3556786176
+                    addr: 4160765952
                   }
-                  {
-                    addr: 2164260864
-                    size: 16777216
-                  }
-                  {
-                    addr: 24092082176
-                    size: 16777216
-                  }
-                  {
-                    addr: 30064771072
-                    size: 16777216
-                  }
-                  {
-                    addr: 4479516672
-                    size: 16777216
-                  }
-                  {
-                    addr: 2952790016
-                    size: 16777216
-                  }
-                  {
-                    addr: 4211081216
-                    size: 16777216
-                  }
-                  {
-                    addr: 4395630592
-                    size: 16777216
-                  }
-                  {
-                    addr: 2466250752
-                    size: 16777216
-                  }
-                  {
-                    addr: 2483027968
-                    size: 16777216
-                  }
-                  {
-                    addr: 269500416
-                    size: 16384
-                  }
                   ...
-                  {
-                    addr: 269811712
-                    size: 32768
-                  }
-                  {
-                    addr: 1895825408
-                    size: 16384
-                  }
-                  {
-                    addr: 1895841792
-                    size: 16384
-                  }
-                  {
-                    addr: 1895858176
-                    size: 16384
-                  }
-                  {
-                    addr: 1879113728
-                    size: 16384
-                  }
-                  {
-                    addr: 1912602624
-                    size: 16384
-                  }
-                  {
-                    addr: 1912619008
-                    size: 16384
-                  }
-                  {
-                    addr: 1912635392
-                    size: 16384
-                  }
-                  {
-                    addr: 1879130112
-                    size: 16384
-                  }
-                  {
-                    addr: 1929379840
-                    size: 16384
-                  }
                   ...
-                  {
-                    addr: 1929396224
-                    size: 16384
-                  }
-                  {
-                    addr: 1929412608
-                    size: 16384
-                  }
-                  {
-                    addr: 1879146496
-                    size: 16384
-                  }
-                  {
-                    addr: 270008320
-                    size: 16384
-                  }
-                  {
-                    addr: 270024704
-                    size: 16384
-                  }
-                  {
-                    addr: 270041088
-                    size: 16384
-                  }
-                  {
-                    addr: 1879162880
-                    size: 16384
-                  }
-                  {
-                    addr: 1879195648
-                    size: 16384
-                  }
-                  {
-                    addr: 1879048192
-                    size: 16384
-                  }
-                  {
-                    addr: 1879212032
-                    size: 16384
-                  }
                   ...
-                  {
-                    addr: 1879179264
-                    size: 16384
-                  }
-                  {
-                    addr: 1879064576
-                    size: 16384
-                  }
-                  {
-                    addr: 1879080960
-                    size: 16384
-                  }
-                  {
-                    addr: 1879097344
-                    size: 16384
-                  }
+                  {
+                    addr: 10483777536
+                    size: 16384
+                  }
                   ...
                 ]
               }
             }
             {
               rsm: {
-                AAPL,phandle: 123
+                AAPL,phandle: 122
-                interrupts: 304
+                interrupts: 302
-                iommu-parent: "}"
+                iommu-parent: "|"
                 reg: [
                   {
-                    addr: 3560067072
+                    addr: 4186066944
                   }
                   {
-                    addr: 3560701952
+                    addr: 4186701824
                   }
                 ]
               }
             }
             {
               dart-rsm: {
-                error-reflector: 11938037760
-                AAPL,phandle: 124
+                AAPL,phandle: 123
                 children: [
                   {
                     mapper-rsm: {
-                      AAPL,phandle: 125
+                      AAPL,phandle: 124
                     }
                   }
                 ]
-                interrupts: 307
+                interrupts: 305
                 reg: {
-                  addr: 3560161280
+                  addr: 4187619328
-                  size: 16384
+                  size: 49152
                 }
               }
             }
             {
               dockchannel-uart: {
-                AAPL,phandle: 126
+                AAPL,phandle: 125
-                interrupts: 432
+                interrupts: 470
                 reg: [
                   {
-                    addr: 3557982208
+                    addr: 4161961984
                   }
                   {
-                    addr: 3557867520
+                    addr: 4161847296
                   }
                 ]
               }
             }
             {
               dockchannel-mtp: {
-                AAPL,phandle: 127
+                AAPL,phandle: 126
                 children: [
                   {
                     mtp-transport: {
+                      fdr-classes: [
+                        "NBCl/NvTM"
+                        "nova-touch-cal"
+                        "NBCl/NvFc"
+                        "nova-force-cal"
+                      ]
+                      fdr-classes-p2: [
+                        "NBCl/NvTh"
+                        "nova-touch-cal"
+                        "NBCl/NvFc"
+                        "nova-force-cal"
+                      ]
-                      AAPL,phandle: 128
+                      AAPL,phandle: 127
                       children: [
                         {
                           multi-touch: {
-                            AAPL,phandle: 129
+                            AAPL,phandle: 128
                             function-clock_enable: [
-                              "4WKp00Pg"
-                              "s"
+                              "8WKpOIcp"
+                              "q"
                             ]
                             function-power_1v2_core: [
-                              "4WKpeDLr"
-                              "s"
+                              "8WKpDLcp"
+                              "q"
                             ]
-                            hid-merge-personality: "F1GE3,1"
+                            hid-merge-personality: "D93S1"
                           }
                         }
+                        {
+                          nova: {
+                            AAPL,phandle: 129
+                            children: [
+                            ]
+                            device_type: "nova"
+                            function-current-read: [
+                              "q"
+                              "8RKpSHcp"
+                              "\""
+                            ]
+                            function-over-current-read: [
+                              "q"
+                              "RyekSMmp"
+                            ]
+                            function-over-current-write: [
+                              "q"
+                              "WyekSMmp"
+                            ]
+                            function-power: [
+                              "q"
+                              "8WKpDLcp"
+                            ]
+                            nova-force-cal: "syscfg/NvFc"
+                            nova-touch-cal: "syscfg/NvTh"
+                          }
+                        }
                       ]
                     }
                   }
                 ]
-                interrupts: 911
+                interrupts: 1137
                 reg: [
                   {
-                    addr: 3937402880
+                    addr: 4373610496
                   }
                   {
-                    addr: 3937484800
+                    addr: 4373692416
                   }
                   {
-                    addr: 3937599488
+                    addr: 4373807104
                   }
                   {
-                    addr: 3937615872
+                    addr: 4373823488
                   }
                   {
-                    addr: 3937566720
+                    addr: 4373774336
                   }
                   {
-                    addr: 3937583104
+                    addr: 4373790720
                   }
                 ]
               }
             }
             {
               mtp: {
-                interrupts: "ngMAAJ0DAACgAwAAnwMAAA=="
+                interrupts: "gQQAAIAEAACDBAAAggQAAA=="
                 reg: [
                   {
-                    addr: 3930062848
+                    addr: 4368367616
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 3926196224
+                    addr: 4362403840
                   }
                 ]
               }
             }
             {
               dart-mtp: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
                 children: [
                   {
                     mapper-mtp: {
-                      reg: 1
+                      reg: 0
                     }
                   }
                 ]
-                dapf-instance-0: "AMAo5AIAAABfwCjkAgAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADFKeQCAAAAp8Yp5AIAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAkAyTkAgAAACcDJOQCAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAAAt5AIAAAATAS3kAgAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBACDAK+QCAAAAI8Ar5AIAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAQwUD0AgAAAB/IQPQCAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIBG9AIAAAADgEb0AgAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADA7vQCAAAAAODu9AIAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQA="
+                dapf-instance-0: "AMAoCAMAAABfwCgIAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAIDEKQgDAAAAJ8YpCAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAEAS0IAwAAABMBLQgDAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAIMArCAMAAAAjwCsIAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBADAAHwgDAAAAMwAfCAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQA4AB8IAwAAADsAHwgDAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAPAAfCAMAAAA/AB8IAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAFAAHwgDAAAAUwAfCAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAQwWAQAwAAAB/IYBADAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIBmEAMAAAADgGYQAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAGRAghADAAAAaECCEAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAwPYQAwAAAADg9hADAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEA"
-                interrupts: 909
+                interrupts: 1135
                 reg: [
                   {
-                    addr: 3934289920
+                    addr: 4370464768
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 3934306304
+                    addr: 4370530304
                   }
                 ]
-                remap: "AgEAAAMBAAAEAQAA"
+                remap: "AQAAAAIAAAADAAAA"
-                sid: 1
+                sid: 0
               }
             }
             ...
             {
               uart0: {
-                clock-gates: "K"
+                clock-gates: "V"
                 function-tx: [
-                  "("
-                  "OIPGk"
+                  "'"
+                  "OIPGP"
                 ]
-                interrupts: 857
+                interrupts: 1092
                 reg: {
-                  addr: 2501902336
+                  addr: 6259998720
                 }
               }
             }
-            {
-              spi3: {
-                #address-cells: 1
-                #size-cells: 7
-                AAPL,phandle: 137
-                children: [
-                  {
-                    audio-codec: {
-                      AAPL,phandle: 138
-                      AOP: "AgADEBAEBAQAAAAA"
-                      DSPDebug: "BAQGGP8EBAQAAAAA"
-                      HPMic: "BAAEGP8EBAQAAAAA"
-                      Hawking: "AwQCEBAEBAQAAAAA"
-                      LPMic: "AQAEEBAEBAQAAAAA"
-                      Receiver: "BAABGP8EBAQAAAAA"
-                      adc-gain: "BgYGBoaGBoaGhgYG"
-                      children: [
-                      ]
-                      clp-ASP: 1
-                      clp-asp-config: "EAMEBQYHCwwNDg8BAgMEBQsMDQ4PAAAA"
-                      compatible: "audio-control,cs42l77"
-                      default-input-data-selectors: "cimicimscimfciml"
-                      device_type: "audio-control"
-                      disable-ANC: null
-                      external-power-provider: "<"
-                      fixed-input-data-selector: null
-                      fixed-sample-rate: null
-                      fmic-mic: 4620
-                      fmic-micbias: 515
-                      function-aop_lpmic: [
-                        "G"
-                        "mpla"
-                      ]
-                      function-dsp-debug1_active: [
-                        "As2i1nip"
-                      ]
-                      function-dsp-debug1_master: [
-                        "1DUAe2pa"
-                      ]
-                      function-ext_mclk_int_mgr: [
-                        "<"
-                        "ltCg"
-                      ]
-                      function-hawk_active: [
-                        "As2i0nip"
-                      ]
-                      function-hawk_master: [
-                        "1DUAh2pa"
-                      ]
-                      function-pdm_rx_control: [
-                        "iMDP"
-                      ]
-                      function-reset: [
-                        "W"
-                      ]
-                      hawking-adc: 14
-                      hawking-adc2: 15
-                      i2c-sda-drive-strength: 67108864
-                      imic-mic: 4106
-                      imic-micbias: 513
-                      interrupt-parent: "("
-                      interrupts: 4294967443
-                      lmic-mic: 4877
-                      lmic-micbias: 516
-                      maximum-asp1-drive-strength: null
-                      pollctl: [
-                        "@"
-                      ]
-                      port-number: 1
-                      port-type: 2
-                      primary-ASP: 4
-                      primary-InMCLK: 1
-                      receiver-pdm: 1
-                      reg: [
-                        {
-                          addr: 356482285568
-                          size: 134283264
-                        }
-                        {
-                          addr: 20
-                        }
-                      ]
-                      routing-source_clp: "ICEfHiMlJCYnIQAA"
-                      routing-source_clp_asp_tx: "WVgeHwAUGhscHQAA"
-                      rx-hac: null
-                      rx-receiver: null
-                      samplerate-default: 206158430208000
-                      secondary-ASP: 2
-                      smic-mic: 4363
-                      smic-micbias: 514
-                      supports-CLP: null
-                    }
-                  }
-                ]
-                clock-gates: "H"
-                clock-ids: 398
-                compatible: "spi-1,spimc"
-                device_type: "spi"
-                function-spi_cs0: [
-                  "("
-                  "OIPG0"
-                ]
-                interrupt-parent: " "
-                interrupts: 868
-                reg: {
-                  addr: 2500902912
-                  size: 16384
-                }
-                spi-version: 1
-              }
-            }
             {
               i2c2: {
-                AAPL,phandle: 139
+                AAPL,phandle: 137
                 children: [
                   {
-                    audio-speaker-top: {
-                      AAPL,phandle: 140
-                      asp-sdout-drive-strength: 4
-                      children: [
-                      ]
-                      compatible: "audio-control,cs35l27"
-                      device-ui32-property-list: "U3BvVNQAAAAQAAAAU3BvVNUAAAD/BwAAU3BvVNYAAAALCQYAU3BvVNsAAAAFAwAAU3BvVNwAAAACBB4AU3BvVNkAAAAAAAAAU3BvVNcAAAAcAAAA"
-                      device_type: "audio-control"
-                      external-power-provider: [
-                        "="
-                        "5"
-                      ]
-                      function-mclk_control: [
-                        "KLCM"
-                      ]
-                      function-reset: [
-                        "("
-                      ]
-                      function-secSpeaker_control: [
-                        "="
-                        "ltCg"
-                      ]
-                      i2c-sda-drive-strength: 2
-                      iboot-audio-volume: 65407
-                      output-datasource-selectors: "StoBSpoT"
-                      reg: {
-                        addr: 10737418240064
-                      }
-                      slot-config: [
-                        " "
-                      ]
-                    }
+                    audio-codec: {
+                      AAPL,phandle: 138
+                      AOP: 67109120
+                      ASP1: 2211958691344
+                      ASP2: 1112396548120
+                      ASP3: 30064789520
+                      ASP4: 18456
+                      Flicker: 34013442
+                      HPMic: 67109121
+                      Hall: 33816834
+                      LPMic: 67109120
+                      Receiver: 16777217
+                      TempSensor: 17170690
+                      adc-gains: "AwMDA4ODA4aGhgAA"
+                      children: [
+                      ]
+                      compatible: "audio-control,cs42l79"
+                      device_type: "audio-control"
+                      flicker-config: 3
+                      fmic-mic: 13036030211
+                      function-Flicker_master: [
+                        "1DUAf2pa"
+                      ]
+                      function-Receiver_master: [
+                        "1DUAr2pa"
+                      ]
+                      function-pdm_rx_control: [
+                        "iMDP"
+                      ]
+                      function-reset: [
+                        "S"
+                      ]
+                      function-reset-pre-p2: [
+                        "S"
+                      ]
+                      halle-calibration: "syscfg/PSCl"
+                      imic-mic: 13002475265
+                      int-id: 2260613153948676
+                      int-offset: 281530996425216
+                      interrupt-parent: "'"
+                      interrupts: 4294967428
+                      lmic-mic: 13052807684
+                      private: "1"
+                      reg: {
+                        addr: 4294967296074
+                      }
+                      samplerate-default: 206158430208000
+                      samplerate-subset: "AAAAAIC7AAAAAAAAAAAAAA=="
+                      smic-mic: 13019252738
+                    }
                   }
                 ]
-                clock-gates: "="
+                clock-gates: "E"
-                filter-tunable: 4842288421776913000
+                filter-tunable: 3545216544722121700
                 function-device_reset: [
                   ...
-                  "TSRA="
+                  "TSRAE"
                 ]
-                interrupts: 882
+                interrupts: 1110
                 reg: {
-                  addr: 2499903488
+                  addr: 6257999872
                 }
-                tbuf-tunable: 4914553097662956000
+                tbuf-tunable: 3459608943045574700
-                trigger-level-tunable: 4914271622686245000
+                trigger-level-tunable: 3458764518115442700
               }
             }
-            {
-              nco: {
-                AAPL,phandle: 38
-                children: [
-                ]
-                clock-ids: "eQEAAHoBAAB3AQAAeAEAAA=="
-                compatible: [
-                  "nco,t8101"
-                  "nco,s5l8960x"
-                ]
-                device_type: "nco"
-                pmgr-nco-page-size: 16384
-                reg: {
-                  addr: 3221504000
-                  size: 81920
-                }
-              }
-            }
             {
               i2c3: {
+                wakeup-device: "mogul-display"
-                AAPL,phandle: 141
+                AAPL,phandle: 139
                 children: [
                   {
                     display-eeprom: {
-                      AAPL,phandle: 142
+                      AAPL,phandle: 140
                       children: [
                         {
                           display-eeprom-data: {
-                            AAPL,phandle: 143
+                            AAPL,phandle: 141
                           }
                         }
                         {
                           display-eeprom-generic-data: {
-                            AAPL,phandle: 144
+                            AAPL,phandle: 142
                           }
                         }
                       ]
                     }
                   }
+                  {
+                    mogul-display: {
+                      AAPL,phandle: 143
+                      children: [
+                      ]
+                      compatible: "mogul,a1222"
+                      iboot-auth: null
+                      ic-auth-type: 196608
+                      reg: {
+                        addr: 10737418240016
+                      }
+                      wakeup-data: "AAAAAEBCDwC4CwAA"
+                    }
+                  }
                 ]
-                clock-gates: ">"
+                clock-gates: "F"
-                filter-tunable: 4842288421776913000
+                filter-tunable: 4846792021404284000
                 function-device_reset: [
                   ...
-                  "TSRA>"
+                  "TSRAF"
                 ]
-                interrupts: 883
+                interrupts: 1111
                 reg: {
-                  addr: 2499919872
+                  addr: 6258016256
                 }
               }
             }
-            {
-              smc-i2c1: {
-                #address-cels: 1
-                #size-cells: 3
-                AAPL,phandle: 145
-                children: [
-                ]
-                clock-gates: 307
-                clock-ids: 4
-                compatible: [
-                  "i2c,t8101"
-                  "i2c,s5l8940x"
-                  "iic,soft"
-                ]
-                device_type: "i2c"
-                filter-tunable: 4842288421776913000
-                function-device_reset: [
-                  "\""
-                ]
-                gpio-iic_scl: [
-                  "SMC"
-                ]
-                gpio-iic_sda: [
-                  "SMC"
-                ]
-                interrupt-parent: " "
-                interrupts: 477
-                reg: {
-                  addr: 3704651776
-                  size: 16384
-                }
-                tbuf-tunable: 4914553097662956000
-                trigger-level-tunable: 4914271622686245000
-              }
-            }
             {
               nub-spmi0: {
+                irq-behavior-map: 69271552
-                AAPL,phandle: 146
+                AAPL,phandle: 144
                 children: [
                   {
                     pmu-main: {
+                      info-has_phra: 1
-                      AAPL,phandle: 147
+                      AAPL,phandle: 145
                       function-external_standby: [
                         ...
-                        "s"
+                        "q"
                       ]
                       function-get_pdod: [
                         ...
-                        "s"
+                        "q"
                       ]
                       function-get_vbus_detect: [
                         ...
-                        "s"
+                        "q"
                       ]
-                      interrupt-parent: 146
+                      interrupt-parent: 144
                     }
                   }
                   {
                     btm: {
-                      AAPL,phandle: 148
+                      AAPL,phandle: 146
-                      interrupt-parent: 146
+                      interrupt-parent: 144
                     }
                   }
                 ]
-                interrupts: "AAEAAMABAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
+                interrupts: "AAEAAOcBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
                 reg: [
                   {
-                    addr: 3564191744
+                    addr: 4168171520
                   }
                   {
-                    addr: 3564126208
+                    addr: 4168105984
                   }
                   {
-                    addr: 3564109824
+                    addr: 4168089600
                   }
                 ]
               }
             }
             {
               nub-spmi1: {
+                irq-behavior-map: 69271552
-                AAPL,phandle: 149
+                AAPL,phandle: 147
                 children: [
                   {
-                    dotaralc: {
-                      AAPL,phandle: 150
-                      children: [
-                      ]
-                      reg: "DAAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
-                    }
+                    shamisen: {
+                      AAPL,phandle: 148
+                      children: [
+                      ]
+                      reg: "DAAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
+                    }
                   }
                   {
                     stonehenge: {
-                      AAPL,phandle: 151
+                      AAPL,phandle: 149
-                      interrupt-parent: 149
+                      interrupt-parent: 147
                     }
                   }
                 ]
-                interrupts: "AAEAAMUBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
+                interrupts: "AAEAAOwBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
                 reg: [
                   {
-                    addr: 3563143168
+                    addr: 4167122944
                   }
                   {
-                    addr: 3563077632
+                    addr: 4167057408
                   }
                   {
-                    addr: 3563061248
+                    addr: 4167041024
                   }
                 ]
               }
             }
             {
               nub-spmi-a0: {
+                irq-behavior-map: 69271552
-                AAPL,phandle: 152
+                AAPL,phandle: 162
                 children: [
                   {
                     spmi-allAce: {
-                      AAPL,phandle: 153
+                      AAPL,phandle: 163
                     }
                   }
                   {
                     spmi-hpm0: {
-                      feature-rf-coex-rf-cl: 8589934593
-                      feature-rf-coex-rf-cl-tout-ms: 25
-                      feature-rf-coex-tp-cl: 21474836483
-                      feature-rf-coex-tp-tout-ms: "2"
-                      AAPL,phandle: 154
+                      AAPL,phandle: 164
-                      aod: 293632478642438400
+                      aod: 293632478642438460
                       children: [
                         {
                           hpm-aid-controller: {
-                            AAPL,phandle: 155
+                            AAPL,phandle: 165
                             children: [
                               {
                                 mogul-mlb: {
-                                  AAPL,phandle: 156
+                                  AAPL,phandle: 166
                                 }
                               }
                               {
-                                mogul-display: {
-                                  AAPL,phandle: 157
-                                  children: [
-                                  ]
-                                  compatible: "aid-component"
-                                  component-function: "auth,display"
-                                  component-type: "mogul,a1222"
-                                  transport-index: 1
-                                  transport-type: 7
-                                }
+                                mogul-display-pre-proto1: {
+                                  AAPL,phandle: 167
+                                  children: [
+                                  ]
+                                  compatible: "aid-component"
+                                  component-function: "auth,display"
+                                  component-type: "mogul,a1222"
+                                  transport-index: 1
+                                  transport-type: 7
+                                }
                               }
                             ]
                           }
                         }
                       ]
-                      dock: 291
+                      dock: 334
-                      features-supported: "AQAAAAIAAAAFAAAA"
+                      features-supported: 8589934593
-                      interrupt-parent: 152
+                      interrupt-parent: 162
                     }
                   }
                 ]
-                interrupts: "AAEAAMcBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
+                interrupts: "AAEAAO4BAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
                 reg: [
                   {
-                    addr: 3566239744
+                    addr: 4170219520
                   }
                   {
-                    addr: 3566223360
+                    addr: 4170203136
                   }
                   {
-                    addr: 3566206976
+                    addr: 4170186752
                   }
                 ]
               }
             }
             {
               aop-spmi0: {
-                use-legacy-spmi-command: null
+                irq-behavior-map: 69271552
-                AAPL,phandle: 158
+                AAPL,phandle: 150
                 children: [
                   {
-                    uwb-heb: {
-                      AAPL,phandle: 159
-                      children: [
-                      ]
-                      reg: "DwAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
-                    }
+                    eclipse-heb: {
+                      AAPL,phandle: 151
+                      children: [
+                      ]
+                      reg: "DgAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
+                    }
                   }
-                  {
-                    wlan-heb: {
-                      AAPL,phandle: 160
-                      children: [
-                      ]
-                      reg: "DgAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
-                    }
-                  }
                   {
                     baseband-heb: {
-                      AAPL,phandle: 161
+                      AAPL,phandle: 152
-                      interrupt-parent: 158
+                      interrupt-parent: 150
                     }
                   }
                   {
                     stockholm-spmi: {
-                      AAPL,phandle: 162
+                      AAPL,phandle: 153
                       children: [
                         {
                           stockholm: {
-                            AAPL,phandle: 163
+                            AAPL,phandle: 154
-                            eos-halley-config: null
+                            eos-halley-config: 1
                             function-enable: [
-                              "4WKp51Pg"
-                              "s"
+                              "8WKpOIcp"
+                              "q"
                             ]
                           }
                         }
                       ]
-                      interrupt-parent: 158
+                      interrupt-parent: 150
                     }
                   }
                   {
                     hammerfest-spmi: {
-                      AAPL,phandle: 164
+                      AAPL,phandle: 155
                       children: [
                         {
                           hammerfest: {
+                            function-enable-pre-p2: [
+                              "S"
+                            ]
-                            AAPL,phandle: 165
+                            AAPL,phandle: 156
                             function-enable: [
-                              "W"
+                              "S"
                             ]
                           }
                         }
                       ]
-                      interrupt-parent: 158
+                      interrupt-parent: 150
                     }
                   }
+                  {
+                    uwb0: {
+                      AAPL,phandle: 157
+                      children: [
+                      ]
+                      reg: "DwAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
+                    }
+                  }
                 ]
-                interrupts: "AAEAAJ0BAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
+                interrupts: "AAEAALABAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
                 reg: [
                   {
-                    addr: 3834200064
+                    addr: 4304486400
                   }
                   {
-                    addr: 3834134528
+                    addr: 4304420864
                   }
                   {
-                    addr: 3834118144
+                    addr: 4304404480
                   }
                 ]
               }
             }
             {
               aop-spmi1: {
+                irq-behavior-map: 69271552
-                AAPL,phandle: 166
+                AAPL,phandle: 158
                 children: [
                   {
-                    uwb-idc: {
-                      AAPL,phandle: 167
-                      children: [
-                      ]
-                      reg: "DwAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
-                    }
+                    uwb: {
+                      AAPL,phandle: 159
+                      children: [
+                      ]
+                      reg: "DwAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
+                    }
                   }
                   {
-                    wlan-idc: {
-                      #num-spmi-interrupts: 1
-                      AAPL,phandle: 168
-                      ar-buffer-addr-rx-e85: 146
-                      children: [
-                      ]
-                      compatible: "wlan,idc"
-                      e85-wlan-freq-bitmask: 128
-                      interrupt-parent: 166
-                      interrupts: 10
-                      irq-tx-offset-e85-start: "<"
-                      irq-tx-offset-e85-stop: "="
-                      reg: "DgAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
-                    }
+                    eclipse-idc: {
+                      AAPL,phandle: 160
+                      children: [
+                      ]
+                      reg: "DgAAAAMAAAAAAAAABAAAAAAAAAAAAAAA"
+                    }
                   }
                   {
                     baseband-idc: {
-                      AAPL,phandle: 169
+                      AAPL,phandle: 161
-                      interrupt-parent: 166
+                      interrupt-parent: 158
                     }
                   }
                 ]
-                interrupts: "AAEAAKEBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
+                interrupts: "AAEAALQBAAAZAQAABAEAAAUBAAAIAQAACQEAAAoBAAAMAQAADQEAABcBAAAYAQAAGgEAABsBAAAcAQAAHQEAABABAAARAQAABgEAAAcBAAALAQAA"
                 reg: [
                   {
-                    addr: 3834462208
+                    addr: 4306583552
                   }
                   {
-                    addr: 3834396672
+                    addr: 4306518016
                   }
                   {
-                    addr: 3834380288
+                    addr: 4306501632
                   }
                 ]
               }
             }
             {
               display-crossbar0: {
-                AAPL,phandle: 170
+                AAPL,phandle: 168
               }
             }
             {
               atc0-dpxbar: {
-                AAPL,phandle: 171
+                AAPL,phandle: 169
                 reg: {
-                  addr: 30115414016
+                  addr: 17364729856
                 }
               }
             }
             {
               atc0-dpphy: {
-                AAPL,phandle: 172
+                AAPL,phandle: 170
-                atc-phy: 173
+                atc-phy: 171
-                compatible: "atc-dpphy,t8130"
+                compatible: "atc-dpphy,t8140"
-                dp-switch-parent: 170
+                dp-switch-parent: 168
-                dpxbar-parent: 171
+                dpxbar-parent: 169
               }
             }
             {
               wdt: {
-                reconfig-wdog-support: null
+                simple-reconfig-wdog-icc-time: 5
+                simple-reconfig-wdog-support: null
+                trigger-ce: [
+                  "x"
+                ]
-                AAPL,phandle: 39
+                AAPL,phandle: 38
                 function-panic_flush_helper: [
-                  ")"
+                  "("
                   ...
                 ]
                 function-panic_halt_helper: [
                   ...
-                  ")"
+                  "("
                 ]
                 function-panic_notify: [
-                  "("
-                  "OIPGI"
+                  "'"
+                  "OIPG5"
                 ]
-                interrupts: 443
+                interrupts: 481
                 reg: [
                   {
-                    addr: 3559587840
+                    addr: 4163567616
                   }
                   {
-                    addr: 3559637520
+                    addr: 4163617316
                   }
                   {
-                    addr: 3559620616
+                    addr: 4163600392
                   }
                   {
-                    addr: 3559620620
+                    addr: 4163600428
                   }
+                  {
+                    addr: 4163600416
+                    size: 4
+                  }
                 ]
               }
             }
             {
               atc-phy0: {
-                compatible: "atc-phy,t8130"
-                dp-training-table-hbr2: [
-                  " p#"
-                ]
-                reg: [
-                  {
-                    addr: 30109401088
-                    size: 16384
-                  }
-                  {
-                    addr: 30106714112
-                    size: 16384
-                  }
-                  {
-                    addr: 30115102720
-                    size: 360448
-                  }
-                  {
-                    addr: 30064771072
-                    size: 16777216
-                  }
-                ]
+                compatible-h17a: "atc-phy,ausbc"
+                compatible-h17p: "atc-phy,t8130"
+                reg-h17a: "AACpCgQAAAAAQAAAAAAAAAAAgAoEAAAAAEAAAAAAAAAAQAQLBAAAAABAAAAAAAAAAAACCwQAAAAAQAAAAAAAAAAAAAgEAAAAAAAAAQAAAAAAAAULBAAAAABAAAAAAAAA"
+                reg-h17p: "AACpCgQAAAAAQAAAAAAAAAAAgAoEAAAAAEAAAAAAAAAAQAQLBAAAAABAAAAAAAAAAAAACwQAAAAAQAAAAAAAAAAIAAsEAAAAAEAAAAAAAAAACgALBAAAAABAAAAAAAAAABAACwQAAAAAQAAAAAAAAAAgAAsEAAAAAEAAAAAAAAAAIgALBAAAAABAAAAAAAAAACYACwQAAAAAQAAAAAAAAAAoAAsEAAAAAEAAAAAAAAAAKgALBAAAAABAAAAAAAAAAEAACwQAAAAAQAAAAAAAAABQAAsEAAAAABAAAAAAAAAAcAALBAAAAABAAAAAAAAAAJAACwQAAAAAQAAAAAAAAACgAAsEAAAAAEAAAAAAAAAAsAALBAAAAABAAAAAAAAAAMAACwQAAAAAQAAAAAAAAADQAAsEAAAAAEAAAAAAAAAAAAELBAAAAABAAAAAAAAAABABCwQAAAAAQAAAAAAAAAAgAQsEAAAAAEAAAAAAAAAAMAELBAAAAABAAAAAAAAAAEABCwQAAAAAQAAAAAAAAABgAQsEAAAAAEAAAAAAAAAAZAELBAAAAABAAAAAAAAAAHABCwQAAAAAQAAAAAAAAACAAQsEAAAAAEAAAAAAAAAAAAILBAAAAABAAAAAAAAAAAAACAQAAAAAAAABAAAAAAAABQsEAAAAAEAAAAAAAAA="
-                AAPL,phandle: 173
+                AAPL,phandle: 171
-                interrupts: 1023
+                interrupts: 1236
               }
             }
             {
               dart-usb: {
-                error-reflector: 11938037760
-                flush-by-dva: 0
-                AAPL,phandle: 174
+                AAPL,phandle: 172
                 children: [
                   {
                     mapper-usb: {
-                      AAPL,phandle: 175
+                      AAPL,phandle: 173
                     }
                   }
                 ]
-                clock-gates: 1924145349056
+                clock-gates: 1374389535040
-                interrupts: 1019
+                interrupts: 1248
                 reg: [
                   {
-                    addr: 30114054144
+                    addr: 17363369984
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 30114578432
+                    addr: 17363894272
-                    size: 16384
+                    size: 49152
                   }
                 ]
               }
             }
             {
               usb-drd: {
+                usb-max-speed-capability: 2
-                AAPL,phandle: 176
+                AAPL,phandle: 174
-                atc-phy-parent: 173
+                atc-phy-parent: 171
                 children: [
                   {
                     usb-drd-port-hs: {
-                      AAPL,phandle: 177
+                      AAPL,phandle: 175
                     }
                   }
                   {
                     usb-drd-port-ss: {
-                      AAPL,phandle: 178
+                      AAPL,phandle: 176
                     }
                   }
                 ]
-                compatible: "usb-drd,t8130"
+                compatible: "usb-drd,t8140"
-                interrupts: "9wMAAPgDAAD5AwAA+gMAAPIDAAA="
+                interrupts: "3AQAAN0EAADeBAAA3wQAANAEAAA="
-                iommu-parent: 175
+                iommu-parent: 173
                 reg: [
                   {
-                    addr: 30100946944
+                    addr: 17350262784
                   }
                   {
-                    addr: 30100422656
+                    addr: 17349738496
                   }
                   {
-                    addr: 30100996096
+                    addr: 17350311936
                   }
                   {
-                    addr: 30109351936
+                    addr: 17358667776
                   }
                   {
-                    addr: 30106714112
+                    addr: 17356029952
                   }
                   {
-                    addr: 30109335552
+                    addr: 17358651392
                   }
                   {
-                    addr: 30098325504
+                    addr: 17348165632
                   }
                   {
-                    addr: 30098849792
+                    addr: 17350316032
                   }
                   {
-                    addr: 30101000192
+                    addr: 17357602816
                   }
                 ]
               }
             }
             {
               dcp: {
+                hdcp-channels: 5
+                hdcp-parent: "\\"
+                idle-ctrl-check: null
-                AAPL,phandle: 179
+                AAPL,phandle: 177
                 children: [
                   {
                     iop-dcp-nub: {
+                      routes: 193
-                      AAPL,phandle: 180
+                      AAPL,phandle: 178
                     }
                   }
                 ]
-                clock-gates: 430
+                clock-gates: 301
-                interrupts: "UgIAAFECAABUAgAAUwIAAA=="
+                interrupts: "qAIAAKcCAACqAgAAqQIAAA=="
-                iommu-parent: 185
+                iommu-parent: 183
-                power-gates: 430
+                power-gates: 301
                 reg: [
                   {
-                    addr: 2126512128
+                    addr: 8638169088
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 2122645504
+                    addr: 8632205312
                   }
+                  {
+                    addr: 8638349312
+                    size: 245768
+                  }
                 ]
               }
             }
             {
               dcp0-expert: {
+                conditional-retention-disable: 3
+                conditional-retention-enable: 4294967296
+                conditional-retention-offset: "jAwAAAAAAADQDAAAAAAAAA=="
+                conditional-retention-size: 2
+                function-enable_autopm: [
+                  "\""
+                ]
+                pmgr-soc-pwrgate-index: 2
+                require-conditional-retention: 1
-                AAPL,phandle: 181
+                AAPL,phandle: 179
                 reg: [
                   {
-                    addr: 3559620676
+                    addr: 4163600452
                   }
                   {
-                    addr: 3556802560
+                    addr: 4160782336
                   }
+                  {
+                    addr: 4034019328
+                    size: 16384
+                  }
                 ]
               }
             }
             {
               disp0: {
-                energy-adder-117: 179568
-                power-lut-data-lut-117: [
-                  "?"
-                  "?"
-                  "@"
-                  "@"
-                  "A"
-                  "A"
-                  "A"
-                  "A"
-                  "A"
-                  "B"
-                  "B"
-                  "B"
-                  "B"
-                  "B"
-                  "B"
-                  "B"
-                  "C"
-                  "D"
-                  "D"
-                  "E"
-                  "E"
-                  "?"
-                  "?"
-                  "A"
-                  "A"
-                  "A"
-                  "B"
-                  "B"
-                  "B"
-                  "C"
-                  "D"
-                  "E"
-                  "F"
-                  "G"
-                  "H"
-                  "H"
-                  "J"
-                  "K"
-                  "L"
-                  "M"
-                  "N"
-                  "N"
-                  "?"
-                  "A"
-                  "A"
-                  "B"
-                  "B"
-                  "D"
-                  "F"
-                  "G"
-                  "I"
-                  "K"
-                  "M"
-                  "O"
-                  "P"
-                  "R"
-                  "T"
-                  "V"
-                  "X"
-                  "Y"
-                  "["
-                  "]"
-                  "^"
-                  "?"
-                  "A"
-                  "B"
-                  "C"
-                  "F"
-                  "H"
-                  "K"
-                  "N"
-                  "Q"
-                  "T"
-                  "V"
-                  "Y"
-                  "\\"
-                  "^"
-                  "a"
-                  "d"
-                  "f"
-                  "i"
-                  "l"
-                  "n"
-                  "q"
-                  "?"
-                  "A"
-                  "C"
-                  "G"
-                  "K"
-                  "O"
-                  "S"
-                  "W"
-                  "["
-                  "_"
-                  "c"
-                  "g"
-                  "k"
-                  "o"
-                  "s"
-                  "w"
-                  "{"
-                  "?"
-                  "B"
-                  "G"
-                  "M"
-                  "S"
-                  "X"
-                  "^"
-                  "d"
-                  "j"
-                  "p"
-                  "v"
-                  "|"
-                  "?"
-                  "C"
-                  "L"
-                  "T"
-                  "\\"
-                  "d"
-                  "m"
-                  "u"
-                  "~"
-                  "?"
-                  "F"
-                  "Q"
-                  "\\"
-                  "g"
-                  "s"
-                  "~"
-                  "?"
-                  "H"
-                  "V"
-                  "b"
-                  "p"
-                  "}"
-                  "?"
-                  "K"
-                  "["
-                  "k"
-                  "{"
-                  "?"
-                  "O"
-                  "b"
-                  "u"
-                  "?"
-                  "Q"
-                  "f"
-                  "{"
-                  "?"
-                  "U"
-                  "n"
-                  "?"
-                  "W"
-                  "q"
-                  "?"
-                  "["
-                  "z"
-                  "?"
-                  "_"
-                  "?"
-                  "b"
-                  "?"
-                  "k"
-                  "?"
-                  "t"
-                  "?"
-                  "|"
-                  "?"
-                  "?"
-                  "?"
-                  "?"
-                  "?"
-                  "?"
-                  "?"
-                  "?"
-                ]
-                power-lut-data-x-117: 28
-                power-lut-data-xindex-117: [
-                  "\""
-                  "2"
-                  "G"
-                  "_"
-                  "p"
-                ]
-                power-lut-data-y-117: 21
-                power-lut-data-yindex-117: "AAAAAAUAAAAKAAAADwAAABQAAAAZAAAAHgAAACMAAAAoAAAALQAAADIAAAA3AAAAPAAAAEEAAABGAAAASwAAAFAAAABVAAAAWgAAAF8AAABkAAAA"
-                power-lut-vbatt-cur-nominal-117: 516
+                energy-adder-151: 114032
+                energy-adder-152: 115998
+                energy-adder-182: 106823
+                function-clock_req_interrupt: [
+                  "\""
+                ]
+                power-lut-data-lut-151: [
+                  "9"
+                  "9"
+                  "9"
+                  ":"
+                  ":"
+                  ":"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  "<"
+                  "<"
+                  "9"
+                  "9"
+                  ":"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  "<"
+                  "="
+                  ">"
+                  "?"
+                  "?"
+                  "@"
+                  "A"
+                  "A"
+                  "B"
+                  "C"
+                  "D"
+                  "9"
+                  ":"
+                  ";"
+                  ";"
+                  ";"
+                  ";"
+                  "="
+                  "?"
+                  "@"
+                  "A"
+                  "B"
+                  "D"
+                  "E"
+                  "G"
+                  "H"
+                  "I"
+                  "K"
+                  "L"
+                  "M"
+                  "O"
+                  "P"
+                  "9"
+                  ";"
+                  ";"
+                  ";"
+                  "="
+                  "?"
+                  "A"
+                  "C"
+                  "F"
+                  "G"
+                  "J"
+                  "L"
+                  "N"
+                  "P"
+                  "R"
+                  "T"
+                  "V"
+                  "X"
+                  "Z"
+                  "\\"
+                  "^"
+                  "9"
+                  ";"
+                  ";"
+                  ">"
+                  "A"
+                  "D"
+                  "G"
+                  "J"
+                  "M"
+                  "P"
+                  "S"
+                  "V"
+                  "Y"
+                  "\\"
+                  "_"
+                  "b"
+                  "e"
+                  "h"
+                  "k"
+                  "n"
+                  "q"
+                  "9"
+                  ";"
+                  ">"
+                  "B"
+                  "G"
+                  "K"
+                  "P"
+                  "T"
+                  "X"
+                  "]"
+                  "a"
+                  "f"
+                  "j"
+                  "o"
+                  "s"
+                  "x"
+                  "|"
+                  "9"
+                  ";"
+                  "A"
+                  "H"
+                  "N"
+                  "T"
+                  "["
+                  "a"
+                  "g"
+                  "n"
+                  "t"
+                  "{"
+                  "9"
+                  "="
+                  "F"
+                  "N"
+                  "V"
+                  "_"
+                  "g"
+                  "p"
+                  "y"
+                  "9"
+                  "?"
+                  "I"
+                  "S"
+                  "\\"
+                  "g"
+                  "q"
+                  "{"
+                  "9"
+                  "A"
+                  "M"
+                  "X"
+                  "e"
+                  "q"
+                  "}"
+                  "9"
+                  "D"
+                  "R"
+                  "`"
+                  "o"
+                  "~"
+                  "9"
+                  "E"
+                  "U"
+                  "e"
+                  "u"
+                  "9"
+                  "H"
+                  "["
+                  "n"
+                  "9"
+                  "I"
+                  "]"
+                  "q"
+                  "9"
+                  "M"
+                  "d"
+                  "{"
+                  "9"
+                  "P"
+                  "i"
+                  "9"
+                  "R"
+                  "n"
+                  "9"
+                  "X"
+                  "{"
+                  "9"
+                  "_"
+                  "9"
+                  "e"
+                  "9"
+                  "l"
+                  "9"
+                  "r"
+                  "9"
+                  "{"
+                  "9"
+                  "~"
+                  "9"
+                  "9"
+                  "9"
+                  "9"
+                ]
+                power-lut-data-lut-152: [
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "A"
+                  ">"
+                  ">"
+                  ">"
+                  "?"
+                  "?"
+                  "?"
+                  "?"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "A"
+                  "B"
+                  "C"
+                  "D"
+                  "D"
+                  "E"
+                  "F"
+                  "G"
+                  "G"
+                  "H"
+                  ">"
+                  ">"
+                  "?"
+                  "?"
+                  "@"
+                  "@"
+                  "A"
+                  "C"
+                  "D"
+                  "E"
+                  "G"
+                  "H"
+                  "J"
+                  "K"
+                  "L"
+                  "N"
+                  "O"
+                  "Q"
+                  "R"
+                  "S"
+                  "T"
+                  ">"
+                  "?"
+                  "?"
+                  "@"
+                  "B"
+                  "D"
+                  "E"
+                  "H"
+                  "J"
+                  "L"
+                  "N"
+                  "P"
+                  "R"
+                  "T"
+                  "V"
+                  "X"
+                  "Z"
+                  "\\"
+                  "^"
+                  "`"
+                  "c"
+                  ">"
+                  "?"
+                  "@"
+                  "C"
+                  "E"
+                  "I"
+                  "L"
+                  "O"
+                  "R"
+                  "U"
+                  "X"
+                  "["
+                  "^"
+                  "a"
+                  "d"
+                  "g"
+                  "j"
+                  "m"
+                  "p"
+                  "s"
+                  "v"
+                  ">"
+                  "?"
+                  "B"
+                  "G"
+                  "K"
+                  "P"
+                  "T"
+                  "Y"
+                  "]"
+                  "b"
+                  "f"
+                  "j"
+                  "o"
+                  "t"
+                  "x"
+                  "}"
+                  ">"
+                  "@"
+                  "F"
+                  "L"
+                  "S"
+                  "Y"
+                  "_"
+                  "f"
+                  "l"
+                  "r"
+                  "y"
+                  ">"
+                  "B"
+                  "J"
+                  "S"
+                  "["
+                  "d"
+                  "l"
+                  "u"
+                  "~"
+                  ">"
+                  "D"
+                  "N"
+                  "X"
+                  "b"
+                  "l"
+                  "v"
+                  ">"
+                  "F"
+                  "R"
+                  "^"
+                  "j"
+                  "w"
+                  ">"
+                  "I"
+                  "X"
+                  "f"
+                  "u"
+                  ">"
+                  "J"
+                  "["
+                  "k"
+                  "|"
+                  ">"
+                  "N"
+                  "a"
+                  "u"
+                  ">"
+                  "O"
+                  "d"
+                  "y"
+                  ">"
+                  "S"
+                  "k"
+                  ">"
+                  "V"
+                  "r"
+                  ">"
+                  "Y"
+                  "x"
+                  ">"
+                  "`"
+                  ">"
+                  "g"
+                  ">"
+                  "n"
+                  ">"
+                  "u"
+                  ">"
+                  "|"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                ]
+                power-lut-data-lut-182: [
+                  "<"
+                  "<"
+                  "<"
+                  "="
+                  "="
+                  "="
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  "?"
+                  "?"
+                  "<"
+                  "<"
+                  "="
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  "?"
+                  "@"
+                  "A"
+                  "B"
+                  "B"
+                  "C"
+                  "D"
+                  "D"
+                  "E"
+                  "F"
+                  "G"
+                  "<"
+                  "="
+                  ">"
+                  ">"
+                  ">"
+                  ">"
+                  "@"
+                  "A"
+                  "C"
+                  "D"
+                  "E"
+                  "G"
+                  "H"
+                  "I"
+                  "K"
+                  "L"
+                  "M"
+                  "O"
+                  "P"
+                  "Q"
+                  "S"
+                  "<"
+                  "="
+                  ">"
+                  ">"
+                  "@"
+                  "B"
+                  "D"
+                  "F"
+                  "H"
+                  "J"
+                  "L"
+                  "O"
+                  "Q"
+                  "S"
+                  "U"
+                  "W"
+                  "Y"
+                  "Z"
+                  "\\"
+                  "_"
+                  "a"
+                  "<"
+                  ">"
+                  ">"
+                  "A"
+                  "D"
+                  "G"
+                  "J"
+                  "M"
+                  "P"
+                  "S"
+                  "V"
+                  "Y"
+                  "\\"
+                  "_"
+                  "b"
+                  "e"
+                  "h"
+                  "k"
+                  "n"
+                  "q"
+                  "t"
+                  "<"
+                  ">"
+                  "A"
+                  "E"
+                  "J"
+                  "N"
+                  "R"
+                  "W"
+                  "["
+                  "`"
+                  "d"
+                  "i"
+                  "m"
+                  "q"
+                  "v"
+                  "{"
+                  "<"
+                  ">"
+                  "D"
+                  "J"
+                  "Q"
+                  "W"
+                  "]"
+                  "d"
+                  "j"
+                  "p"
+                  "w"
+                  "}"
+                  "<"
+                  "@"
+                  "H"
+                  "Q"
+                  "Y"
+                  "b"
+                  "j"
+                  "s"
+                  "{"
+                  "<"
+                  "B"
+                  "K"
+                  "U"
+                  "_"
+                  "i"
+                  "s"
+                  "~"
+                  "<"
+                  "D"
+                  "P"
+                  "["
+                  "h"
+                  "t"
+                  "<"
+                  "F"
+                  "U"
+                  "c"
+                  "r"
+                  "<"
+                  "H"
+                  "X"
+                  "h"
+                  "x"
+                  "<"
+                  "K"
+                  "^"
+                  "q"
+                  "<"
+                  "L"
+                  "`"
+                  "t"
+                  "<"
+                  "P"
+                  "f"
+                  "~"
+                  "<"
+                  "R"
+                  "l"
+                  "<"
+                  "U"
+                  "q"
+                  "<"
+                  "["
+                  "~"
+                  "<"
+                  "a"
+                  "<"
+                  "h"
+                  "<"
+                  "o"
+                  "<"
+                  "u"
+                  "<"
+                  "~"
+                  "<"
+                  "<"
+                  "<"
+                  "<"
+                  "<"
+                ]
+                power-lut-data-x-151: 28
+                power-lut-data-x-152: 28
+                power-lut-data-x-182: 28
+                power-lut-data-xindex-151: [
+                  "\""
+                  "2"
+                  "G"
+                  "_"
+                  "p"
+                ]
+                power-lut-data-xindex-152: [
+                  "\""
+                  "2"
+                  "G"
+                  "_"
+                  "p"
+                ]
+                power-lut-data-xindex-182: [
+                  "\""
+                  "2"
+                  "G"
+                  "_"
+                  "p"
+                ]
+                power-lut-data-y-151: 21
+                power-lut-data-y-152: 21
+                power-lut-data-y-182: 21
+                power-lut-data-yindex-151: "AAAAAAUAAAAKAAAADwAAABQAAAAZAAAAHgAAACMAAAAoAAAALQAAADIAAAA3AAAAPAAAAEEAAABGAAAASwAAAFAAAABVAAAAWgAAAF8AAABkAAAA"
+                power-lut-data-yindex-152: "AAAAAAUAAAAKAAAADwAAABQAAAAZAAAAHgAAACMAAAAoAAAALQAAADIAAAA3AAAAPAAAAEEAAABGAAAASwAAAFAAAABVAAAAWgAAAF8AAABkAAAA"
+                power-lut-data-yindex-182: "AAAAAAUAAAAKAAAADwAAABQAAAAZAAAAHgAAACMAAAAoAAAALQAAADIAAAA3AAAAPAAAAEEAAABGAAAASwAAAFAAAABVAAAAWgAAAF8AAABkAAAA"
+                power-lut-vbatt-cur-nominal-151: 372
+                power-lut-vbatt-cur-nominal-152: 403
+                power-lut-vbatt-cur-nominal-182: 373
-                AAPL,phandle: 182
+                AAPL,phandle: 180
                 children: [
                   {
                     hilo: {
-                      AAPL,phandle: 183
+                      AAPL,phandle: 181
                     }
                   }
                 ]
-                clock-gates: "XgEAAF4BAABfAQAAYAEAAA=="
+                clock-gates: "9AAAAPQAAAD1AAAA9gAAAA=="
-                compatible: "disp0,t8130"
+                compatible: "disp0,t8140"
-                energy-adder: 152043
+                energy-adder: 111411
                 function-bw_req_interrupt0: [
                   ...
-                  "QRIB["
+                  "QRIB:"
                 ]
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
-                interrupts: "XAIAAG8CAABfAgAAXgIAAF0CAABkAgAAWgIAAGgCAABjAgAA"
+                interrupts: "sQIAAMQCAAC0AgAAswIAALICAAC5AgAArwIAAL0CAAC4AgAA"
-                iommu-parent: 807453851835
+                iommu-parent: 803158884538
-                power-gates: "XgEAAF4BAABfAQAAYAEAAA=="
+                power-gates: "9AAAAPQAAAD1AAAA9gAAAA=="
                 power-lut-data-lut: [
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "@"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "A"
+                  "B"
+                  "B"
+                  "B"
+                  "B"
+                  "C"
+                  "C"
+                  "C"
+                  "C"
+                  "D"
+                  "D"
+                  "D"
+                  "D"
+                  "E"
+                  "E"
+                  "E"
+                  "E"
+                  "E"
+                  "E"
+                  "E"
+                  "F"
+                  "F"
+                  "F"
+                  "F"
+                  "G"
+                  "G"
+                  "G"
+                  "H"
+                  "H"
+                  "I"
+                  "I"
+                  "I"
+                  "I"
+                  "J"
+                  "J"
+                  "J"
+                  "K"
+                  "K"
+                  "K"
+                  "L"
+                  "L"
+                  "L"
+                  "L"
+                  "M"
+                  "M"
+                  "M"
+                  "N"
+                  "N"
+                  "N"
+                  "O"
+                  "O"
+                  "P"
+                  "P"
+                  "P"
+                  "P"
+                  "P"
+                  "P"
+                  "Q"
+                  "Q"
+                  "R"
+                  "R"
                   ...
                   ...
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "S"
-                  "U"
-                  "U"
-                  "U"
-                  "V"
-                  "V"
-                  "V"
-                  "V"
-                  "V"
-                  "V"
+                  "T"
+                  "T"
+                  "T"
+                  "U"
+                  "U"
+                  "U"
+                  "U"
                   ...
                   ...
                   ...
                   ...
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "W"
-                  "X"
-                  "X"
-                  "X"
-                  "X"
-                  "X"
                   ...
                   ...
                   ...
-                  "Y"
+                  "Z"
+                  "Z"
                   ...
                   ...
                   ...
-                  "["
-                  "["
-                  "\\"
-                  "\\"
-                  "\\"
-                  "\\"
-                  "\\"
-                  "]"
-                  "]"
+                  "\\"
+                  "\\"
+                  "\\"
+                  "\\"
                   ...
                   ...
                   ...
-                  "_"
-                  "`"
-                  "`"
+                  "^"
                   ...
                   ...
                   ...
                   ...
                   ...
-                  "b"
-                  "b"
-                  "b"
                   ...
-                  "c"
-                  "d"
-                  "d"
-                  "d"
+                  "d"
+                  "d"
+                  "d"
+                  "d"
+                  "e"
                   ...
                   ...
                   ...
                   ...
-                  "g"
                   ...
                   ...
-                  "i"
-                  "i"
-                  "j"
                   ...
                   ...
                   ...
                   ...
-                  "k"
                   ...
-                  "l"
+                  "m"
+                  "m"
+                  "m"
+                  "m"
                   ...
                   ...
                   ...
                   ...
                   ...
                   ...
-                  "p"
-                  "q"
-                  "r"
-                  "r"
                   ...
                   ...
                   ...
-                  "s"
                   ...
-                  "t"
-                  "v"
+                  "u"
                   ...
                   ...
-                  "x"
-                  "x"
+                  "y"
                   ...
                   ...
                   ...
                   ...
-                  "|"
-                  "|"
-                  "}"
+                  "{"
+                  "{"
+                  "{"
                   ...
+                  "~"
+                  "~"
                 ]
-                power-lut-vbatt-cur-nominal: 528
+                power-lut-vbatt-cur-nominal: 337
                 reg: [
                   {
-                    addr: 2080374784
+                    addr: 8589934592
-                    size: 7487488
+                    size: 11517952
                   }
                   {
-                    addr: 2088763392
+                    addr: 8625848320
-                    size: 7487488
+                    size: 65536
                   }
                   {
-                    addr: 2100428800
+                    addr: 8627322880
                   }
                   {
-                    addr: 2100559872
+                    addr: 8627339264
                   }
-                  {
-                    addr: 2100576256
-                    size: 16384
-                  }
                   {
-                    addr: 2122317824
+                    addr: 8631877632
                   }
-                  {
-                    addr: 3225223168
-                    size: 16384
-                  }
+                  {
+                    addr: 4068474880
+                    size: 770048
+                  }
                 ]
               }
             }
             {
               dart-dcp: {
-                apf-bypass-15: null
-                error-reflector: 11938037760
-                flush-by-dva: 0
+                exclave-sid: 24
+                vm-base-24: 2199023255552
+                vm-size-23: 68719476736
+                vm-size-24: 1099511627776
-                AAPL,phandle: 184
+                AAPL,phandle: 182
                 children: [
                   {
                     mapper-dcp: {
-                      AAPL,phandle: 185
+                      AAPL,phandle: 183
-                      reg: 5
+                      reg: 23
                     }
                   }
+                  {
+                    mapper-dcp-exclave: {
+                      AAPL,phandle: 184
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 24
+                    }
+                  }
                 ]
-                interrupts: 613
+                interrupts: 698
                 reg: {
-                  addr: 2100346880
+                  addr: 8626896896
-                  size: 16384
+                  size: 49152
                 }
-                remap: 5527622911238
+                remap: 25409026529051
-                sid: 64424509445
+                sid: 64424509463
-                sid-count: 16
+                sid-count: 29
-                vm-size: 68719476736
+                vm-size: 3298534883328
               }
             }
             {
               dart-disp0: {
-                apf-bypass-15: null
-                bypass-15: null
-                error-reflector: 11938037760
+                exclave-sid: 17179869187
+                manual-availability: 1
+                remap: "AQAAAAcAAAAIAAAACQAAAAoAAAAbAAAAEhAAAA=="
+                tlbi-flushes-smmu: null
+                vm-alignment: "AQAAAAgAAAAIAAAA"
+                vm-base-3: 1099511627776
+                vm-base-4: 1099511627776
+                vm-size-0: 68719476736
+                vm-size-16: 68719476736
+                vm-size-3: 68719476736
+                vm-size-4: 68719476736
-                AAPL,phandle: 186
+                AAPL,phandle: 185
                 children: [
                   {
                     mapper-disp0: {
-                      AAPL,phandle: 187
+                      AAPL,phandle: 186
                     }
                   }
                   {
                     mapper-disp0-piodma: {
-                      AAPL,phandle: 188
+                      AAPL,phandle: 187
-                      reg: 4
+                      reg: 16
                     }
                   }
+                  {
+                    mapper-disp0-scl: {
+                      AAPL,phandle: 188
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 3
+                    }
+                  }
+                  {
+                    mapper-disp0-sca: {
+                      AAPL,phandle: 189
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 4
+                    }
+                  }
                 ]
-                interrupts: 613
+                interrupts: 698
                 reg: [
                   {
-                    addr: 2100314112
+                    addr: 8626634752
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 2100297728
+                    addr: 8626716672
                   }
                 ]
-                sid: "AAAAAAQAAAAPAAAA"
+                sid: 68719476736
-                sid-count: 16
+                sid-count: 29
-                vm-size: 68719476736
+                vm-size: 3298534883328
               }
             }
             {
               dart-dispgrt: {
-                apf-bypass-15: null
-                bypass-15: null
-                error-reflector: 11938037760
+                bypass-8: null
+                manual-availability: 1
+                remap: 2057
+                tlbi-flushes-smmu: null
-                AAPL,phandle: 189
+                AAPL,phandle: 190
                 children: [
                   {
                     mapper-dispgrt: {
-                      AAPL,phandle: 190
+                      AAPL,phandle: 191
-                      reg: 0
+                      reg: 8
                     }
                   }
                 ]
-                interrupts: 613
+                interrupts: 698
                 reg: [
                   {
-                    addr: 2100625408
+                    addr: 8626765824
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 2100609024
+                    addr: 8626847744
                   }
                 ]
-                sid: 64424509440
+                sid: 8
               }
             }
             {
               dcp-sac-controller: {
-                AAPL,phandle: 191
+                AAPL,phandle: 192
               }
             }
             {
               gpio: {
-                glitchless: 1
-                #gpio-pins: 217
+                #gpio-pins: 216
-                AAPL,phandle: 40
+                AAPL,phandle: 39
-                interrupts: "DAEAAA0BAAAOAQAADwEAABABAAARAQAAEgEAAA=="
+                interrupts: "BwEAAAgBAAAJAQAACgEAAAsBAAAMAQAADQEAAA=="
                 reg: {
-                  addr: 3071279104
+                  addr: 4462739456
                 }
               }
             }
             {
               dispext0: {
+                function-clock_req_interrupt: [
+                  "\""
+                ]
-                AAPL,phandle: 192
+                AAPL,phandle: 196
-                compatible: "dispext0,t8130"
+                compatible: "dispext0,t8140"
                 function-bw_req_interrupt0: [
                   ...
-                  "QRIB\\"
+                  "QRIB;"
                 ]
-                interrupts: "lgIAAKkCAACZAgAAmAIAAJcCAACeAgAAlAIAAJ0CAAA="
+                interrupts: "+QIAAAwDAAD8AgAA+wIAAAEDAAD3AgAAAAMAAA=="
-                iommu-parent: 858993459399
+                iommu-parent: 880468295884
                 reg: [
                   {
-                    addr: 4429185024
+                    addr: 8657043456
-                    size: 7372800
+                    size: 11517952
                   }
                   {
-                    addr: 4437573632
+                    addr: 8692957184
-                    size: 7372800
+                    size: 65536
                   }
                   {
-                    addr: 4449239040
+                    addr: 8694448128
                   }
-                  {
-                    addr: 4449386496
-                    size: 16384
-                  }
                   {
-                    addr: 4471128064
+                    addr: 8698986496
                   }
-                  {
-                    addr: 3225223168
-                    size: 16384
-                  }
+                  {
+                    addr: 4068474880
+                    size: 770048
+                  }
                 ]
               }
             }
             {
               dcpext-expert: {
+                pmgr-soc-pwrgate-index: 2
-                AAPL,phandle: 193
+                AAPL,phandle: 197
                 reg: [
                   {
-                    addr: 3559620676
+                    addr: 4163600452
                   }
                   {
-                    addr: 3556802560
+                    addr: 4160782336
                   }
+                  {
+                    addr: 4034019328
+                    size: 16384
+                  }
                 ]
               }
             }
             {
               dcpext: {
+                idle-ctrl-check: null
-                AAPL,phandle: 194
+                AAPL,phandle: 198
-                audio: 201
+                audio: 206
                 children: [
                   {
                     iop-dcpext-nub: {
+                      port-number: 1
+                      port-type: 2
-                      AAPL,phandle: 195
+                      AAPL,phandle: 199
                     }
                   }
                 ]
-                clock-gates: 431
+                clock-gates: 302
-                dp-switch-parent: 170
+                dp-switch-parent: 168
-                dp-switch-ufp-endpoint: 0
+                dp-switch-ufp-endpoint: 1
-                hdcp-parent: "`"
+                hdcp-parent: "\\"
-                interrupts: "jwIAAI4CAACRAgAAkAIAAA=="
+                interrupts: "8AIAAO8CAADyAgAA8QIAAA=="
-                iommu-parent: 197
+                iommu-parent: 867583393993
-                power-gates: 431
+                power-gates: 302
                 reg: [
                   {
-                    addr: 4475322368
+                    addr: 8705277952
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 4471455744
+                    addr: 8699314176
                   }
+                  {
+                    addr: 8705458176
+                    size: 245768
+                  }
                 ]
               }
             }
             {
               dart-dcpext0: {
-                apf-bypass-15: null
-                bypass-15: null
-                error-reflector: 11938037760
+                exclave-sid: 24
+                remap: 25409026529051
+                vm-size-23: 68719476736
-                AAPL,phandle: 196
+                AAPL,phandle: 200
                 children: [
                   {
                     mapper-dcpext0: {
-                      AAPL,phandle: 197
+                      AAPL,phandle: 201
-                      reg: 5
+                      reg: 23
                     }
                   }
+                  {
+                    mapper-dcpext0-exclave: {
+                      AAPL,phandle: 202
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 24
+                    }
+                  }
                 ]
-                flush-by-dva: 0
+                flush-by-dva: 1
-                interrupts: 671
+                interrupts: 770
                 reg: {
-                  addr: 4449157120
+                  addr: 8694005760
-                  size: 16384
+                  size: 49152
                 }
-                sid: 64424509445
+                sid: 23
-                sid-count: 16
+                sid-count: 29
-                vm-size: 68719476736
+                vm-size: 3298534883328
               }
             }
             {
               dart-dispext0: {
-                apf-bypass-15: null
-                bypass-15: null
-                error-reflector: 11938037760
+                manual-availability: 1
+                remap: "AQAAAAcAAAAIAAAACQAAAAoAAAAbAAAAEhAAAA=="
+                tlbi-flushes-smmu: null
+                vm-alignment: "AQAAAAgAAAAIAAAA"
-                AAPL,phandle: 198
+                AAPL,phandle: 203
                 children: [
                   {
                     mapper-dispext0: {
-                      AAPL,phandle: 199
+                      AAPL,phandle: 204
                     }
                   }
                   {
                     mapper-dispext0-piodma: {
-                      AAPL,phandle: 200
+                      AAPL,phandle: 205
-                      reg: 4
+                      reg: 16
                     }
                   }
                 ]
-                interrupts: 671
+                interrupts: 770
                 reg: [
                   {
-                    addr: 4449124352
+                    addr: 8693743616
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 4449107968
+                    addr: 8693825536
                   }
                 ]
-                sid: "AAAAAAQAAAAPAAAA"
+                sid: 68719476736
-                sid-count: 16
+                sid-count: 29
               }
             }
             {
               dp-audio1: {
-                AAPL,phandle: 201
+                AAPL,phandle: 206
-                clock-gates: "T"
+                clock-gates: "]"
-                dma-parent: "i"
+                dma-parent: "h"
                 function-device_reset_dpa: [
                   ...
-                  "TSRAT"
+                  "TSRA]"
                 ]
-                power-gates: "T"
+                power-gates: "]"
               }
             }
             {
               scaler0: {
-                AAPL,phandle: 202
+                AAPL,phandle: 207
                 clock-gates: [
-                  "0"
+                  "="
                 ]
                 function-device_reset: [
                   ...
-                  "TSRA,"
+                  "TSRA1"
                 ]
-                hardware-version: 19
+                hardware-version: 22
-                interrupts: 3663607104339
+                interrupts: 4672924419134
-                iommu-parent: 880468295884
+                iommu-parent: 901943132369
-                perf-clocks: 12884901888
+                perf-clocks: 8589934592
                 power-gates: [
-                  "0"
+                  "="
                 ]
                 reg: [
                   {
-                    addr: 4513071104
+                    addr: 2164260864
-                    size: 196608
+                    size: 229376
                   }
                   {
-                    addr: 4515233792
+                    addr: 2166423552
                   }
                   {
-                    addr: 4515184640
+                    addr: 2166374400
                   }
+                  {
+                    addr: 2147483648
+                    size: 32768
+                  }
                 ]
               }
             }
             {
               dart-scaler: {
-                error-reflector: 11938037760
-                AAPL,phandle: 203
+                AAPL,phandle: 208
                 children: [
                   {
                     mapper-scaler: {
-                      AAPL,phandle: 204
+                      AAPL,phandle: 209
                     }
                   }
                   {
                     mapper-scaler-piodma: {
-                      AAPL,phandle: 205
+                      AAPL,phandle: 210
                     }
                   }
                 ]
-                interrupts: 852
+                interrupts: 1087
                 reg: {
-                  addr: 4515168256
+                  addr: 2166751232
-                  size: 16384
+                  size: 131072
                 }
               }
             }
-            {
-              jpeg0: {
-                AAPL,phandle: 206
-                children: [
-                ]
-                clock-gates: "pQEAAIUBAACGAQAA"
-                clock-ids: 1387274436930
-                compatible: [
-                  "jpeg,t8101"
-                  "jpeg,s5l8920x"
-                ]
-                coprovider-group: "jpeg"
-                device_type: "jpeg"
-                hw-type: "100000"
-                interrupt-parent: " "
-                interrupts: 843
-                iommu-parent: 208
-                power-gates: "pQEAAIUBAACGAQAA"
-                reg: {
-                  addr: 2365587456
-                  size: 16384
-                }
-              }
-            }
-            {
-              dart-jpeg0: {
-                AAPL,phandle: 207
-                children: [
-                  {
-                    mapper-jpeg0: {
-                      AAPL,phandle: 208
-                      children: [
-                      ]
-                      compatible: "iommu-mapper"
-                      device_type: "dart-mapper"
-                      reg: 0
-                    }
-                  }
-                ]
-                compatible: "dart,t8110"
-                dart-options: "%"
-                device_type: "dart"
-                error-reflector: 11938037760
-                flush-by-dva: 1
-                instance: [
-                  "TRAD"
-                  "DART"
-                ]
-                interrupt-parent: " "
-                interrupts: 844
-                page-size: 16384
-                reg: {
-                  addr: 2365603840
-                  size: 16384
-                }
-                sid: 0
-                sid-count: 1
-                vm-base: 1099511627776
-                vm-size: 3298534883328
-              }
-            }
             {
               mcc: {
-                config-data: [
-                  "d"
-                  "d"
-                  "d"
-                  "d"
-                  "d"
-                ]
-                dcs-enable-thermal-loop: 1
-                dcs_num_channels: 4
-                mcache-pmp: 1
-                panic-save-ce: 1
-                pmp_ptd_reg_idx: 5
-                pmp_ptd_update_space_offset: 65536
-                ptd-ranges: 128849018894
-                ptd-ranges-smc: "D"
+                amcc-count: 1
+                amcc-reg-idx: 2
+                dcs-count-per-amcc: 4
+                mcw-reg-idx: 1
+                panic-save-reg-idx: 0
+                pmp_ptd_db_reg_idx: 6
+                pmp_ptd_update_reg_idx: 7
+                ptd-range-ctrl2drv: 30
+                ptd-range-drv2ctrl: 14
+                skip-mcc-off-to-s2r: 1
+                socni-count: 3
+                socni-reg-idx: 3
-                AAPL,phandle: 41
+                AAPL,phandle: 40
-                compatible: "mcc,t8130"
+                compatible: "mcc,t8140"
                 reg: [
-                  {
-                    addr: 269484032
-                    size: 540672
-                  }
+                  {
+                    addr: 4030529536
+                    size: 16384
+                  }
                   {
-                    size: 1048576
+                    size: 788529152
                   }
-                  {
-                    addr: 272629760
-                    size: 16777216
-                  }
                   {
-                    addr: 272367616
+                    addr: 1056997376
-                    size: 1048576
+                    size: 32768
                   }
                   {
-                    addr: 3229089792
+                    addr: 4034396160
                   }
                   {
-                    addr: 3225157632
+                    addr: 1090551808
-                    size: 196608
+                    size: 32768
                   }
+                  {
+                    addr: 4031217664
+                    size: 5276
+                  }
+                  {
+                    addr: 1073774592
+                    size: 32768
+                  }
+                  {
+                    addr: 4030464000
+                    size: 16384
+                  }
                 ]
               }
             }
-            {
-              jpeg1: {
-                AAPL,phandle: 209
-                children: [
-                ]
-                clock-gates: "pgEAAIUBAACGAQAA"
-                clock-ids: 1387274436930
-                compatible: [
-                  "jpeg,t8101"
-                  "jpeg,s5l8920x"
-                ]
-                coprovider-group: "jpeg"
-                device_type: "jpeg"
-                hw-type: "100000"
-                interrupt-parent: " "
-                interrupts: 846
-                iommu-parent: 211
-                power-gates: "pgEAAIUBAACGAQAA"
-                reg: {
-                  addr: 2365636608
-                  size: 16384
-                }
-              }
-            }
-            {
-              dart-jpeg1: {
-                AAPL,phandle: 210
-                children: [
-                  {
-                    mapper-jpeg1: {
-                      AAPL,phandle: 211
-                      children: [
-                      ]
-                      compatible: "iommu-mapper"
-                      device_type: "dart-mapper"
-                      reg: 0
-                    }
-                  }
-                ]
-                compatible: "dart,t8110"
-                dart-options: "%"
-                device_type: "dart"
-                error-reflector: 11938037760
-                flush-by-dva: 1
-                instance: [
-                  "TRAD"
-                  "DART"
-                ]
-                interrupt-parent: " "
-                interrupts: 847
-                page-size: 16384
-                reg: {
-                  addr: 2365652992
-                  size: 16384
-                }
-                sid: 0
-                sid-count: 1
-                vm-base: 1099511627776
-                vm-size: 3298534883328
-              }
-            }
             {
               ispRtb: {
-                function-mcc_dataset: [
-                  ")"
-                  "SD$M"
-                ]
-                AAPL,phandle: 212
+                AAPL,phandle: 222
                 children: [
                   {
                     iop-isp-nub: {
-                      AAPL,phandle: 213
+                      AAPL,phandle: 223
                     }
                   }
                 ]
                 clock-gates: [
-                  " "
-                  "o"
+                  "m"
                 ]
-                compatible: "iop-isp,ascwrap-v6"
+                compatible: [
+                  "iop-isp,ascwrap-v6"
+                  "isp,s5l8960x"
+                ]
                 function-bw_req_interrupt: [
+                  " "
                   ...
-                  "QRIB4"
+                  "QRIB7"
                 ]
                 function-clock_req_interrupt: [
+                  "!"
                   ...
-                  "QRIC4"
+                  "QRIC7"
                 ]
                 function-device_reset: [
                   ...
-                  "TSRA4"
+                  "TSRA7"
                 ]
-                interrupts: "OgEAADkBAAA8AQAAOwEAAEEBAABCAQAAQwEAAEQBAAA="
+                interrupts: "NAEAADMBAAA2AQAANQEAAEMBAABEAQAARQEAAEYBAABQAQAA"
-                iommu-parent: 932007903448
+                iommu-parent: "4gAAAOMAAADkAAAA5QAAAOYAAADnAAAA"
                 power-gates: [
-                  " "
-                  "o"
+                  "m"
                 ]
                 reg: [
                   {
-                    addr: 2302672896
+                    addr: 4586471424
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 2298806272
+                    addr: 4580507648
                   }
                   {
-                    addr: 2281701376
+                    addr: 4563402752
                   }
                   {
-                    addr: 2281701376
+                    addr: 4563402752
-                    size: 67108864
+                    size: 67010560
                   }
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
                   {
-                    addr: 3228712960
+                    addr: 4034019328
                   }
                 ]
-                sensor-type: "C"
+                sensor-type: "E"
               }
             }
             {
               isp: {
+                exclave-assigned: null
+                exclave-edk-endpoint: 24
+                exclave-endpoint: 23
-                AAPL,phandle: 214
+                AAPL,phandle: 224
-                clock-gates: [
-                  " "
-                ]
+                clock-gates: "JwEAABsAAAAcAAAA/gAAAA=="
                 compatible: [
-                  "isp,generic"
-                  "isp,isp-generic-1"
+                  "isp,isp-generic-ex"
                   ...
                 ]
                 function-bw_req_interrupt: [
+                  " "
                   ...
-                  "QRIB4"
+                  "QRIB7"
                 ]
                 function-campmu_reset: [
-                  "("
-                  "OIPGe"
+                  "'"
+                  "OIPGK"
                 ]
                 function-clock_req_interrupt: [
+                  "!"
                   ...
-                  "QRIC4"
+                  "QRIC7"
                 ]
                 function-device_reset: [
                   ...
-                  "TSRA4"
+                  "TSRA7"
                 ]
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
                 function-sensor_extclk: [
-                  "("
+                  "'"
                 ]
                 function-sensor_extclk2: [
-                  "("
+                  "'"
                 ]
-                interrupts: "QQEAAEIBAABDAQAARAEAAA=="
+                interrupts: "QwEAAEQBAABFAQAARgEAAFABAAA="
-                iommu-parent: 932007903448
+                iommu-parent: "4gAAAOMAAADkAAAA5QAAAOYAAADnAAAA"
-                power-gates: [
-                  " "
-                ]
+                power-gates: "JwEAABsAAAAcAAAA/gAAAA=="
                 reg: [
                   {
-                    addr: 2281701376
+                    addr: 4563402752
-                    size: 67108864
+                    size: 67010560
                   }
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
                   {
-                    addr: 3228712960
+                    addr: 4034019328
                   }
                 ]
-                sensor-type: "C"
+                sensor-type: "E"
               }
             }
             {
               dart-isp: {
-                error-reflector: 11938037760
+                exclave-sid: "BAAAAAUAAAAIAAAACQAAAA=="
+                remap: "AQAAAAIAAAADAAAABgAAAAcAAAAKAAAACwAAAA=="
-                AAPL,phandle: 215
+                AAPL,phandle: 225
                 children: [
                   {
                     mapper-isp: {
-                      AAPL,phandle: 216
+                      AAPL,phandle: 226
-                      iomd-cache-size: 1024
+                      iomd-cache-size: 4000
-                      iomd-cache-ttl: 2000
+                      iomd-cache-ttl: 3000
                     }
                   }
                   {
                     mapper-isp-mpm: {
-                      AAPL,phandle: 217
+                      AAPL,phandle: 227
-                      reg: 11
+                      reg: 12
                     }
                   }
+                  {
+                    mapper-isp-epipe0-exclave: {
+                      AAPL,phandle: 228
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      iomd-cache-size: 1024
+                      iomd-cache-ttl: 3000
+                      reg: 4
+                    }
+                  }
+                  {
+                    mapper-isp-epipe1-exclave: {
+                      AAPL,phandle: 229
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      iomd-cache-size: 1024
+                      iomd-cache-ttl: 3000
+                      reg: 5
+                    }
+                  }
+                  {
+                    mapper-isp-piodma0-exclave: {
+                      AAPL,phandle: 230
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      iomd-cache-size: 1024
+                      iomd-cache-ttl: 3000
+                      reg: 8
+                    }
+                  }
+                  {
+                    mapper-isp-piodma1-exclave: {
+                      AAPL,phandle: 231
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      iomd-cache-size: 1024
+                      iomd-cache-ttl: 3000
+                      reg: 9
+                    }
+                  }
                 ]
-                dapf-instance-0: "AEBw0AIAAABjQHDQAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAc9ACAAAA/z9z0AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAwMPQAgAAAAPAw9ACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAMBC9AIAAAADwEL0AgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACARPQCAAAAA4BE9AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAAEYRAwAAAAMARhEDAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEAAIAIAAAD8YwEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABABCACAAAA/GMFIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQAggAgAAAPxjCSACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEAMIAIAAAD8Yw0gAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAPCACAAAA/GM9IAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAAD3QAgAAAAAQPdACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEABIAIAAAD7YwEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAA=="
+                dapf-instance-0: "AEBwAAMAAABjQHAAAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAcwADAAAA/z9zAAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAwOMAAwAAAAPA4wADAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAMBiEAMAAAADgGQQAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAAAAZgEEAAAAAwBmAQQAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQAAgAgAAAPxiASACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEAEIAIAAAD8YgUgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABACCACAAAA/GIJIAIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAQAwgAgAAAPxiDSACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAEAQIAIAAAD8YhEgAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAABAggIDAAAABECCAgMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQAAADwAAwAAAABAPgADAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEA"
-                interrupts: 326
+                interrupts: 341
                 reg: [
                   {
-                    addr: 2320154624
+                    addr: 4606132224
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 2320203776
+                    addr: 4606263296
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 2320236544
+                    addr: 4606394368
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 2320187392
+                    addr: 4606345216
                   }
                   {
-                    addr: 2320220160
+                    addr: 4606476288
                   }
                   {
-                    addr: 2320171008
+                    addr: 4606197760
                   }
                 ]
-                sid: "AAAAAAsAAAAPAAAA"
+                sid: 51539607552
-                vm-size: 3758096384
+                vm-size: 4026531840
               }
             }
             {
               ave: {
+                coprovider-group: "ave"
+                sve-id: 0
-                AAPL,phandle: 218
+                AAPL,phandle: 233
                 clock-gates: [
+                  "w"
+                  "x"
                   ...
                   ...
                   ...
-                  "|"
-                  "}"
                 ]
-                clock-ids: 402
+                clock-ids: 417
                 function-clock_req_interrupt: [
                   ...
-                  "QRIC-"
+                  "#"
+                  "QRIC2"
                 ]
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
-                interrupts: "BQMAAP8CAAD+AgAAAQMAAAADAAA="
+                interrupts: "vgMAALgDAAC3AwAAugMAALkDAAA="
-                iommu-parent: 220
+                iommu-parent: 235
                 power-gates: [
+                  "w"
+                  "x"
                   ...
                   ...
                   ...
-                  "|"
-                  "}"
                 ]
                 reg: [
                   {
-                    addr: 4379901952
+                    addr: 1963982848
                   }
                   {
-                    addr: 4387241984
+                    addr: 1971322880
                   }
                   {
-                    addr: 4379181056
+                    addr: 1963261952
                   }
                   {
-                    addr: 3228598272
+                    addr: 4033904640
                   }
                   {
-                    addr: 4362076160
+                    addr: 1946157056
                   }
                 ]
-                soc-id: "t8130"
+                soc-id: "t8140"
               }
             }
             {
               dart-ave: {
-                allow-mixed-bypass-mode: null
-                bypass-15: 8858370048
-                error-reflector: 11938037760
+                bypass-12: null
+                dapf-instance-1: "EMHgiQIAAAAfiOKJAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAA=="
-                AAPL,phandle: 219
+                AAPL,phandle: 234
                 children: [
                   {
                     mapper-ave: {
-                      AAPL,phandle: 220
+                      AAPL,phandle: 235
-                      iomd-cache-size: 128
+                      iomd-cache-size: 512
                     }
                   }
                 ]
-                interrupts: 770
+                interrupts: 955
                 reg: [
                   {
-                    addr: 4379049984
+                    addr: 1963458560
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 4379115520
+                    addr: 1963589632
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 4378984448
+                    addr: 1963540480
                   }
                   {
-                    addr: 4379131904
+                    addr: 1963655168
                   }
                 ]
-                sid: 64424509440
+                sid: 51539607552
               }
             }
             {
               avd: {
-                AAPL,phandle: 221
+                AAPL,phandle: 239
-                clock-gates: "owEAAIMBAACEAQAA"
+                clock-gates: "IgEAAPoAAAD7AAAA"
                 function-avd_reset: [
                   ...
-                  "TSRA."
+                  "TSRA8"
                 ]
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
-                interrupts: 3229815407343
+                interrupts: 4024384357288
-                iommu-parent: "3wAAAOAAAADhAAAA"
+                iommu-parent: "8QAAAPIAAADzAAAA"
-                power-gates: "owEAAIMBAACEAQAA"
+                power-gates: "IgEAAPoAAAD7AAAA"
-                reg: {
-                  addr: 2013265920
-                  size: 20987904
-                }
+                reg: [
+                  {
+                    addr: 6174015488
+                    size: 20987904
+                  }
+                  {
+                    addr: 4161241088
+                    size: 16384
+                  }
+                ]
               }
             }
             {
               dart-avd: {
-                error-reflector: 11938037760
-                AAPL,phandle: 222
+                AAPL,phandle: 240
                 children: [
                   {
                     mapper-avd: {
-                      AAPL,phandle: 223
+                      AAPL,phandle: 241
                     }
                   }
                   {
                     mapper-avd-piodma: {
-                      AAPL,phandle: 224
+                      AAPL,phandle: 242
                     }
                   }
                   {
                     mapper-avd-adsbuf: {
-                      AAPL,phandle: 225
+                      AAPL,phandle: 243
                     }
                   }
                 ]
-                interrupts: 758
+                interrupts: 943
                 reg: {
-                  addr: 2030108672
+                  addr: 6190923776
-                  size: 16384
+                  size: 131072
                 }
               }
             }
             {
               ane: {
-                ptd-ranges: "F"
+                exclave-assigned: null
+                exclave-edk-endpoint: 26
+                exclave-endpoint: 25
+                pmp-virt-notify: 1
-                AAPL,phandle: 226
+                AAPL,phandle: 244
-                ane-type: 208
+                ane-type: 512
-                clock-gates: 420
+                clock-gates: 1451698946339
-                compatible: "ane,t8020"
+                compatible: "ane,t8132exclave"
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
-                interrupts: 580
+                interrupts: 2869038154383
-                iommu-parent: 983547511012
+                iommu-parent: 1090921693430
-                power-gates: 420
+                power-gates: 1451698946339
                 reg: [
                   {
-                    addr: 4294967296
+                    addr: 8321499136
                   }
                   {
-                    addr: 3228565504
+                    addr: 4033871872
                   }
                   {
-                    addr: 3228712960
+                    addr: 4034019328
                   }
                   {
-                    addr: 3225157632
+                    addr: 4030464000
                   }
+                  {
+                    addr: 16777216
+                    size: 16728064
+                  }
+                  {
+                    addr: 4163665920
+                    size: 16384
+                  }
                 ]
               }
             }
             {
               error-handler: {
+                afi-ns-names: " 0SN"
+                amcc-metadata: [
+                  "ccma"
+                ]
+                dcs-metadata: [
+                  " scd"
+                ]
+                function-mcc_dataset: [
+                  "("
+                  "SD$M"
+                ]
+                ni0-metadata: "IDBpbgkAAAABAAAAEgAAAAEAAAAAAAAA"
+                ni1-metadata: "IDFpbgoAAAABAAAAEwAAAAEAAAAAAAAA"
+                ni2-metadata: "IDJpbgsAAAABAAAAFAAAAAEAAAAAAAAA"
+                ni3-metadata: "IDNpbgwAAAABAAAAFQAAAAEAAAAAAAAA"
+                nsi-metadata: "IGlzbg0AAAABAAAAFgAAAAEAAAAAAAAA"
+                pio-metadata: "IG9pcA4AAAABAAAAFwAAAAEAAAAAAAAA"
+                pmgr-metadata: "cmdtcAMAAAAGAAAABAAAAAEAAAAAAAAA"
+                ptd-ranges-smc: "D"
+                sep-metadata: "IHBlcwEAAAACAAAABQAAAAkAAAAAAAAA"
-                AAPL,phandle: 42
+                AAPL,phandle: 41
-                compatible: "error-handler,t8130"
+                compatible: "error-handler,t8140"
-                error-reflector: 11938037760
+                error-reflector: 10720641024
-                interrupts: "HgEAAEwBAABNAQAAVQEAACABAAAkAQAAKAEAACwBAAAjAQAAJwEAACsBAAAvAQAA"
+                interrupts: "GgEAABwBAAAeAQAAIAEAAHwDAABgAQAAaQEAAF8BAABmAQAAYgEAAGMBAABkAQAAZwEAAGUBAAAiAQAAJQEAACgBAAArAQAAsQAAALIAAACzAAAAtAAAALUAAAC2AAAA"
                 reg: [
-                  {
-                    addr: 269484032
-                    size: 1048576
-                  }
-                  {
-                    addr: 268976128
-                    size: 98304
-                  }
-                  {
-                    addr: 269221888
-                    size: 4096
-                  }
-                  {
-                    addr: 269336576
-                    size: 49152
-                  }
-                  {
-                    addr: 269238272
-                    size: 98304
-                  }
                   {
-                    addr: 272564224
+                    addr: 4034035712
                   }
                   {
-                    addr: 2430861312
+                    addr: 1892679680
                   }
-                  {
-                    addr: 2430599168
-                    size: 262144
-                  }
-                  {
-                    addr: 2426421248
-                    size: 4
-                  }
                   {
-                    addr: 3221225472
+                    addr: 4026531840
                   }
-                  {
-                    addr: 3228729344
-                    size: 16384
-                  }
                   {
-                    size: 4096
+                    size: 788529152
                   }
-                  {
-                    addr: 3559768064
-                    size: 98304
-                  }
-                  {
-                    addr: 3228991488
-                    size: 16384
-                  }
                   {
-                    addr: 272629760
+                    addr: 4060086272
                   }
+                  {
+                    addr: 4030529536
+                    size: 16384
+                  }
+                  {
+                    addr: 4034297856
+                    size: 16384
+                  }
+                  {
+                    addr: 1056964608
+                    size: 16384
+                  }
+                  {
+                    addr: 1073741824
+                    size: 16384
+                  }
+                  {
+                    addr: 1090519040
+                    size: 16384
+                  }
+                  {
+                    addr: 1107296256
+                    size: 16384
+                  }
+                  {
+                    addr: 1124114432
+                    size: 2468
+                  }
                   {
-                    addr: 268550144
+                    addr: 1888485376
-                    size: 49152
+                    size: 32768
                   }
-                  {
-                    addr: 268451840
-                    size: 98304
-                  }
-                  {
-                    addr: 268697600
-                    size: 4096
-                  }
-                  {
-                    addr: 268812288
-                    size: 49152
-                  }
+                  {
+                    addr: 1140850688
+                    size: 131072
+                  }
                   {
-                    addr: 268713984
+                    addr: 4163747840
                   }
-                  {
-                    addr: 268959744
-                    size: 4096
-                  }
-                  {
-                    addr: 269074432
-                    size: 49152
-                  }
                 ]
               }
             }
             {
               dart-ane: {
-                bypass-15: null
-                error-reflector: 11938037760
+                exclave-sid: "AQAAAAIAAAADAAAABAAAAAUAAAAGAAAABwAAAA=="
-                AAPL,phandle: 227
+                AAPL,phandle: 245
                 children: [
                   {
                     mapper-ane: {
-                      AAPL,phandle: 228
+                      AAPL,phandle: 246
                     }
                   }
                   {
                     mapper-ane-mpm: {
-                      AAPL,phandle: 229
+                      AAPL,phandle: 254
                     }
                   }
+                  {
+                    mapper-ane-iso1: {
+                      AAPL,phandle: 247
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 1
+                    }
+                  }
+                  {
+                    mapper-ane-iso2: {
+                      AAPL,phandle: 248
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 2
+                    }
+                  }
+                  {
+                    mapper-ane-iso3: {
+                      AAPL,phandle: 249
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 3
+                    }
+                  }
+                  {
+                    mapper-ane-iso4: {
+                      AAPL,phandle: 250
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 4
+                    }
+                  }
+                  {
+                    mapper-ane-iso5: {
+                      AAPL,phandle: 251
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 5
+                    }
+                  }
+                  {
+                    mapper-ane-iso6: {
+                      AAPL,phandle: 252
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 6
+                    }
+                  }
+                  {
+                    mapper-ane-iso7: {
+                      AAPL,phandle: 253
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      reg: 7
+                    }
+                  }
                 ]
-                dapf-instance-0: "AIBGmQIAAAADgEaZAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADAcNACAAAAG8Bw0AIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQBwA3DQAgAAAHMDcNACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEADGFy0AIAAAAPYXLQAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAACARpICAAAAA4BGkgIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQA="
+                dapf-instance-0: "AIBmIQMAAAADgGYhAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAADAcAADAAAAE8BwAAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAQCQAnAAAwAAAJMCcAADAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwEAAIBmggQAAAADgGaCBAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAA=="
-                interrupts: 581
+                interrupts: 656
                 reg: [
                   {
-                    addr: 4320133120
+                    addr: 8346664960
-                    size: 16384
+                    size: 49152
                   }
                   {
-                    addr: 4320198656
+                    addr: 8346796032
-                    size: 16384
+                    size: 131072
                   }
                   {
-                    addr: 4320264192
+                    addr: 8346927104
-                    size: 16384
+                    size: 131072
                   }
                   {
-                    addr: 4320149504
+                    addr: 8346730496
                   }
                 ]
               }
             }
             {
               apr: {
-                AAPL,phandle: 230
+                AAPL,phandle: 255
                 clock-gates: [
-                  "/"
+                  "4"
                 ]
-                compatible: "apr,g0"
+                compatible: "apr,k0"
                 function-device_reset: [
                   ...
-                  "TSRA/"
+                  "TSRA4"
                 ]
-                interrupts: 4423816315911
+                interrupts: 5407363826924
-                iommu-parent: 232
+                iommu-parent: 257
                 reg: [
                   {
-                    addr: 4412407808
+                    addr: 2231369728
                   }
                   {
-                    addr: 4395630592
+                    addr: 2214592512
                   }
                 ]
               }
             }
             {
               dart-apr: {
-                error-reflector: 11938037760
-                AAPL,phandle: 231
+                AAPL,phandle: 256
                 children: [
                   {
                     mapper-apr: {
-                      AAPL,phandle: 232
+                      AAPL,phandle: 257
                     }
                   }
                 ]
-                interrupts: 1028
+                interrupts: 1257
                 reg: {
-                  addr: 4412440576
+                  addr: 2231500800
-                  size: 16384
+                  size: 131072
                 }
               }
             }
             {
               sgx: {
-                gpu-avg-power-filter-tc-ms: 248
-                gpu-avg-power-ki-only: 1106247680
-                gpu-avg-power-kp: 1082549862
-                gpu-avg-power-min-duty-cycle: "("
-                gpu-avg-power-target-filter-tc: 1
-                gpu-fast-die0-alarm-threshold: "X"
-                gpu-fast-die0-integral-gain: 1142063104
-                gpu-fast-die0-proportional-gain: 1101183058
-                gpu-fast-die0-sensor-mask: 2
-                gpu-fast-die0-target: "X"
-                gpu-perf-boost-ce-step: "\""
-                gpu-perf-boost-min-util: "d"
-                gpu-perf-filter-drop-threshold: 0
-                gpu-perf-filter-time-constant: 5
-                gpu-perf-filter-time-constant2: "}"
-                gpu-perf-integral-gain: 1074412913
-                gpu-perf-integral-gain2: 1074412913
-                gpu-perf-integral-min-clamp: 0
-                gpu-perf-proportional-gain: "fff@"
-                gpu-perf-proportional-gain2: "fff@"
-                gpu-ppm-filter-time-constant-ms: 16
-                gpu-ppm-ki: 1137180672
-                gpu-ppm-kp: 1056964608
-                gpu-pwr-filter-time-constant: 313
-                gpu-pwr-integral-gain: 1017484678
-                gpu-pwr-integral-min-clamp: 0
-                gpu-pwr-min-duty-cycle: "("
-                gpu-pwr-proportional-gain: 1084821467
-                gpu-se-engagement-criteria: 525
-                gpu-se-filter-time-constant: 9
-                gpu-se-filter-time-constant-1: 3
-                gpu-se-inactive-threshold: 2500
-                gpu-se-ki: 3259498496
-                gpu-se-ki-1: 3267887104
-                gpu-se-kp: 3231711232
-                gpu-se-kp-1: 3231711232
-                gpu-se-reset-criteria: "2"
-                gpu-se-tgt: 1400
-                gpu-sochot-temp: "l"
-                AAPL,phandle: 233
+                AAPL,phandle: 258
-                clock-gates: 1468878815573
+                clock-gates: 1013612282091
-                compatible: "gpu,t8130"
+                compatible: "gpu,t8140"
                 function-mcc_dataset: [
-                  ")"
+                  "("
                   ...
                 ]
-                interrupts: "CgMAAAsDAAAMAwAADQMAAB8DAAAhAwAAGQMAAA=="
+                interrupts: "zwMAANADAADRAwAA0gMAAOkDAADrAwAA3gMAAOADAAA="
-                interrupts-valid: "_"
+                interrupts-valid: 223
-                power-gates: 1468878815573
+                power-gates: 1013612282091
                 reg: [
                   {
-                    addr: 2147483648
+                    addr: 10468982784
                   }
                   {
-                    addr: 2161115136
+                    addr: 10482614272
                   }
                 ]
               }
             }
             {
               gfx-asc: {
-                AAPL,phandle: 234
+                AAPL,phandle: 259
                 children: [
                   {
                     iop-gfx-nub: {
-                      power-managed: "true"
+                      user-power-managed: "true"
-                      AAPL,phandle: 235
+                      AAPL,phandle: 260
                     }
                   }
                 ]
-                clock-gates: 343
+                clock-gates: 237
-                interrupts: "HAMAABsDAAAeAwAAHQMAAA=="
+                interrupts: "4gMAAOEDAADkAwAA4wMAAA=="
-                iommu-parent: 236
+                iommu-parent: 263
-                power-gates: 343
+                power-gates: 237
                 reg: [
                   {
-                    addr: 2185232384
+                    addr: 10508828672
-                    size: 442368
+                    size: 557056
                   }
                   {
-                    addr: 2181365760
+                    addr: 10502864896
                   }
                 ]
               }
             }
             {
               mapper-gfx-asc: {
-                AAPL,phandle: 236
+                AAPL,phandle: 263
               }
             }
             {
-              admac-aop-audio: {
-                #dma-channels: 16
-                AAPL,phandle: 237
-                channel-buffer-allocation: 12288
-                channels-offset: 0
-                children: [
-                ]
-                clock-ids: 1168231104785
-                compatible: "admac,t8130"
-                device_type: "admac"
-                external-power: null
-                interrupt-parent: " "
-                interrupts: 419
-                iommu-parent: "T"
-                irq-destination-index: 2
-                irq-destinations: "UPCAUPCS CIAKLCS"
-                light-my-fire: null
-                night-on-fire: 1026048216
-                reg: [
-                  {
-                    addr: 3835166720
-                    size: 212992
-                  }
-                  {
-                    addr: 3559555072
-                    size: 8
-                  }
-                ]
-                role: " APA"
-              }
+              dart-ave1: {
+                AAPL,phandle: 237
+                bypass-12: null
+                children: [
+                  {
+                    mapper-ave1: {
+                      AAPL,phandle: 238
+                      children: [
+                      ]
+                      compatible: "iommu-mapper"
+                      device_type: "dart-mapper"
+                      iomd-cache-size: 512
+                      iomd-cache-ttl: 2000
+                      reg: 0
+                    }
+                  }
+                ]
+                compatible: "dart,t8110"
+                dapf-instance-1: "EMHghQIAAAAfiOKFAgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMBAA=="
+                dart-options: "%"
+                device_type: "dart"
+                flush-by-dva: 1
+                instance: [
+                  "TRAD"
+                  "DART"
+                  "CPUDART"
+                  "UMMS"
+                  "SMMU"
+                  "CPU_DAPF"
+                ]
+                interrupt-parent: " "
+                interrupts: 967
+                page-size: 16384
+                reg: [
+                  {
+                    addr: 2030567424
+                    size: 49152
+                  }
+                  {
+                    addr: 2030698496
+                    size: 49152
+                  }
+                  {
+                    addr: 2030649344
+                    size: 16384
+                  }
+                  {
+                    addr: 2030764032
+                    size: 16384
+                  }
+                ]
+                remap: 1
+                sid: 51539607552
+                sid-count: 16
+                vm-base: 1099511627776
+                vm-size: 3298534883328
+              }
             }
-            {
-              admac-aop-base: {
-                #dma-channels: 8
-                AAPL,phandle: 238
-                channel-buffer-allocation: 8192
-                channels-offset: 0
-                children: [
-                ]
-                compatible: "admac,t8130"
-                device_type: "admac"
-                interrupt-parent: " "
-                interrupts: 418
-                iommu-parent: "U"
-                irq-destination-index: 2
-                irq-destinations: "UPCAUPCS CIAKLCS"
-                reg: [
-                  {
-                    addr: 3834642432
-                    size: 212992
-                  }
-                  {
-                    addr: 3559555072
-                    size: 8
-                  }
-                ]
-                role: " BPA"
-              }
-            }
-            {
-              admac-sio: {
-                #dma-channels: 12
-                AAPL,phandle: 239
-                channel-buffer-allocation: 16384
-                channels-offset: "("
-                children: [
-                ]
-                clock-gates: [
-                  "Q"
-                ]
-                clock-ids: 1443109011847
-                compatible: "admac,t8130"
-                device_type: "admac"
-                interrupt-parent: " "
-                interrupts: 879
-                iommu-parent: "m"
-                irq-destination-index: 1
-                irq-destinations: "UPCS CIADSNUKLCS"
-                power-gates: [
-                  "Q"
-                ]
-                reg: [
-                  {
-                    addr: 2535456768
-                    size: 212992
-                  }
-                  {
-                    addr: 3559555072
-                    size: 8
-                  }
-                ]
-                role: " OIS"
-              }
-            }
-            {
-              sio-mca-pmgr: {
-                AAPL,phandle: 240
-                children: [
-                ]
-                clock-gates: [
-                  "V"
-                  "W"
-                  "X"
-                  "Y"
-                ]
-                compatible: "mca-pmgr,t8130"
-                device_type: "mca-pmgr"
-                mcawrap-inactive-mask: "0"
-                reg: {
-                  addr: 3221487796
-                  size: 16
-                }
-                soc-location: "/ois"
-              }
-            }
             {
               dwi: {
-                AAPL,phandle: 43
+                AAPL,phandle: 42
-                clock-gates: 18
+                clock-gates: 13
-                interrupts: 16
+                interrupts: 23
                 reg: {
-                  addr: 3223322624
+                  addr: 4028628992
                 }
               }
             }
-            {
-              sio-mca-switch: {
-                AAPL,phandle: 241
-                children: [
-                ]
-                compatible: "mca-switch,t8130"
-                device_type: "mca-switch"
-                function-mca_pmgr: [
-                  "gmpm"
-                ]
-                mca-identity: ".0ws"
-                numClusters: 4
-                reg: [
-                  {
-                    addr: 2537553920
-                    size: 98304
-                  }
-                  {
-                    addr: 2536505344
-                    size: 131072
-                  }
-                ]
-                regStride: "AEAAAABAAAAEAAAABAAAAA=="
-                soc-location: "/ois"
-              }
-            }
-            {
-              sio-mca0: {
-                #address-cells: 0
-                #size-cells: 12
-                AAPL,phandle: 242
-                children: [
-                  {
-                    sio-mca0a: {
-                      AAPL,phandle: 243
-                      children: [
-                        {
-                          audio-codec-hawking: {
-                            AAPL,phandle: 244
-                            children: [
-                            ]
-                            compatible: "audio-data,hawking"
-                            data-sources: [
-                              "Codec"
-                            ]
-                            device_type: "audio-data"
-                            reg: "ABIAAA8QAQAAAAAA+gABADAAAQAAAAAAMAAAAAACEBAAAAAA"
-                            registerWithPrimary: null
-                          }
-                        }
-                      ]
-                      clock-domain: "niam"
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        ")"
-                        "!"
-                        ")"
-                        "\""
-                      ]
-                      dma-parent: 239
-                      external-power-provider: 239
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "8QAAAFJzMmkwZHVhMG5pcAEBAQA="
-                      mca-identity: "a0cm"
-                    }
-                  }
-                ]
-                compatible: "mcaCluster,t8130"
-                device_type: "i2s"
-                function-switch_config: [
-                  "Cacm.0lc"
-                ]
-                interrupt-parent: " "
-                interrupts: 872
-                mca-identity: ".0lc"
-                reg: [
-                  {
-                    addr: 2537553920
-                    size: 16384
-                  }
-                  {
-                    addr: 2536505344
-                    size: 16384
-                  }
-                  {
-                    addr: 2536521728
-                    size: 16384
-                  }
-                ]
-              }
-            }
-            {
-              sio-mca1: {
-                #address-cells: 0
-                #size-cells: 12
-                AAPL,phandle: 245
-                children: [
-                  {
-                    sio-mca1a: {
-                      AAPL,phandle: 246
-                      children: [
-                        {
-                          audio-codec: {
-                            AAPL,phandle: 247
-                            children: [
-                            ]
-                            compatible: "audio-data,cs42l77"
-                            device_type: "audio-data"
-                            reg: [
-                              "0"
-                            ]
-                          }
-                        }
-                      ]
-                      clock-domain: "niam"
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        ","
-                        "!"
-                        "`"
-                        "-"
-                        "!"
-                        ","
-                        "\""
-                        "`"
-                        "-"
-                        "\""
-                      ]
-                      dma-parent: 239
-                      external-power-provider: 239
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "8QAAAFJzMmkyZHVhMW5pcAMDAwA="
-                      mca-identity: "a1cm"
-                      mclk-config: 1
-                    }
-                  }
-                  {
-                    sio-mca1b: {
-                      AAPL,phandle: 248
-                      children: [
-                        {
-                          audio-dsp-debug1: {
-                            AAPL,phandle: 249
-                            children: [
-                            ]
-                            compatible: "audio-data,dsp-debug1"
-                            data-sources: [
-                              "e2pa`"
-                              "}"
-                              "DSP_Debug1"
-                            ]
-                            device_type: "audio-data"
-                            ignoreDataSourceCount: null
-                            reg: "ABIAAAoYAQAAAAAA+gABADAAAQAAAAAA8AMAAAAGGBgAAAAA"
-                            registerWithPrimary: null
-                            usePrimaryWorkloop: null
-                          }
-                        }
-                      ]
-                      clock-domain: "niam"
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        "/"
-                        "!"
-                        "/"
-                        "\""
-                      ]
-                      dma-parent: 239
-                      external-power-provider: 239
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "8QAAAFJzMmkzZHVhMW5pcAMDAQA="
-                      mca-identity: "b1cm"
-                    }
-                  }
-                ]
-                compatible: "mcaCluster,t8130"
-                device_type: "i2s"
-                function-switch_config: [
-                  "Cacm.1lc"
-                ]
-                interrupt-parent: " "
-                interrupts: 873
-                mca-identity: ".1lc"
-                reg: [
-                  {
-                    addr: 2537570304
-                    size: 16384
-                  }
-                  {
-                    addr: 2536538112
-                    size: 16384
-                  }
-                  {
-                    addr: 2536554496
-                    size: 16384
-                  }
-                ]
-              }
-            }
-            {
-              sio-mca2: {
-                #address-cells: 0
-                #size-cells: 12
-                AAPL,phandle: 250
-                children: [
-                  {
-                    sio-mca2a: {
-                      AAPL,phandle: 251
-                      children: [
-                        {
-                          audio-loopback: {
-                            AAPL,phandle: 252
-                            children: [
-                            ]
-                            compatible: "audio-data,audio-loopback"
-                            data-sources: [
-                              "Loopback"
-                            ]
-                            device_type: "audio-data"
-                            reg: [
-                              "0"
-                            ]
-                          }
-                        }
-                      ]
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        "0"
-                        "!"
-                        "1"
-                        "!"
-                        "0"
-                        "\""
-                        "1"
-                        "\""
-                      ]
-                      dma-parent: 239
-                      external-power-provider: 239
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "8QAAAFJzMmk0Lnh0Mm5pcAICAgA="
-                      function-i2s_route0: "8QAAAFJzMmk0LnhyNC54dAEBAAA="
-                      mca-identity: "a2cm"
-                      mclk-config: -4294967294
-                      syncGen-config: "2nys2gkc2nys2gkc"
-                    }
-                  }
-                ]
-                compatible: "mcaCluster,t8130"
-                device_type: "i2s"
-                function-switch_config: [
-                  "Cacm.2lc"
-                ]
-                interrupt-parent: " "
-                interrupts: 874
-                mca-identity: ".2lc"
-                reg: [
-                  {
-                    addr: 2537586688
-                    size: 16384
-                  }
-                  {
-                    addr: 2536570880
-                    size: 16384
-                  }
-                  {
-                    addr: 2536587264
-                    size: 16384
-                  }
-                ]
-              }
-            }
-            {
-              aop-mca-pmgr: {
-                AAPL,phandle: 253
-                children: [
-                ]
-                compatible: "mca-pmgr,t8130"
-                device_type: "mca-pmgr"
-                function-aop-device-control2: [
-                  "D"
-                  "ltCg"
-                ]
-                function-aop-device-control2-id: "cp2m"
-                function-aop-device-control3: [
-                  "E"
-                  "ltCg"
-                ]
-                function-aop-device-control3-id: "cp3m"
-                mcawrap-inactive-mask: "3"
-                reg: {
-                  addr: 3559129108
-                  size: 8
-                }
-                soc-location: "/poa"
-              }
-            }
             {
-              aop-mca-switch: {
-                AAPL,phandle: 254
-                children: [
-                ]
-                compatible: "mca-switch,t8130"
-                device_type: "mca-switch"
-                function-mca_pmgr: [
-                  "gmpm"
-                ]
-                mca-identity: ".0ws"
-                numClusters: 4
-                reg: [
-                  {
-                    addr: 3833593856
-                    size: 65536
-                  }
-                  {
-                    addr: 3835740160
-                    size: 131072
-                  }
-                ]
-                regStride: "AEAAAABAAAAEAAAABAAAAA=="
-                soc-location: "/poa"
-              }
+              gfx1-asc: {
+                AAPL,phandle: 261
+                children: [
+                  {
+                    iop-gfx1-nub: {
+                      AAPL,phandle: 262
+                      children: [
+                      ]
+                      compatible: "iop-nub,rtbuddy-v2"
+                      coredump-enable: "@"
+                      coredump-rel-privacy-approved: null
+                      firmware-name: "GFX1"
+                      no-firmware-service: null
+                      power-managed: "true"
+                      shutdown-sleep: null
+                    }
+                  }
+                ]
+                clock-gates: 321
+                clock-ids: 351
+                compatible: "iop,ascwrap-v6"
+                device_type: "gfx-asc"
+                interrupt-parent: " "
+                interrupts: "5gMAAOUDAADoAwAA5wMAAA=="
+                iommu-parent: 263
+                iop-version: 1
+                power-gates: 321
+                reg: [
+                  {
+                    addr: 10517217280
+                    size: 557056
+                  }
+                  {
+                    addr: 10511253504
+                    size: 8
+                  }
+                ]
+                role: "GFX1"
+              }
             }
-            {
-              aop-mca2: {
-                #address-cells: 0
-                #size-cells: 12
-                AAPL,phandle: 255
-                children: [
-                  {
-                    aop-mca2a: {
-                      AAPL,phandle: 256
-                      children: [
-                        {
-                          audio-aop-loopback: {
-                            AAPL,phandle: 257
-                            children: [
-                            ]
-                            compatible: "audio-data,audio-aop-mca-loopback"
-                            data-sources: [
-                              "AOP Loopback"
-                            ]
-                            device_type: "audio-data"
-                            reg: [
-                              "0"
-                            ]
-                          }
-                        }
-                      ]
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        "!"
-                        "!"
-                        "\""
-                        "\""
-                      ]
-                      dma-parent: 238
-                      external-power-provider: [
-                        "D"
-                      ]
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "/gAAAFJzMmk0Lnh0Mm5pcAICAgA="
-                      function-i2s_route0: "/gAAAFJzMmk0LnhyNC54dAEBAAA="
-                      mca-identity: "a2cm"
-                    }
-                  }
-                ]
-                compatible: "mcaCluster,t8130"
-                device_type: "i2s"
-                function-switch_config: [
-                  "Cacm.2lc"
-                ]
-                interrupt-parent: " "
-                interrupts: 370
-                mca-identity: ".2lc"
-                reg: [
-                  {
-                    addr: 3833626624
-                    size: 16384
-                  }
-                  {
-                    addr: 3835805696
-                    size: 16384
-                  }
-                  {
-                    addr: 3835822080
-                    size: 16384
-                  }
-                ]
-              }
-            }
             {
-              aop-mca3: {
-                #address-cells: 0
-                #size-cells: 12
-                AAPL,phandle: 258
-                children: [
-                  {
-                    aop-mca3a: {
-                      AAPL,phandle: 259
-                      children: [
-                        {
-                          audio-speaker-top: {
-                            AAPL,phandle: 260
-                            children: [
-                            ]
-                            compatible: "audio-data,cs35l27"
-                            device_type: "audio-data"
-                            reg: [
-                              "0"
-                            ]
-                          }
-                        }
-                      ]
-                      clock-domain: "niam"
-                      compatible: "mca,t8130"
-                      device_type: "i2s"
-                      dma-channels: [
-                        "!"
-                        "!"
-                        "\""
-                        "\""
-                      ]
-                      dma-parent: 238
-                      external-power-provider: [
-                        "E"
-                      ]
-                      function-admac_powerswitch: [
-                        "CSPa"
-                      ]
-                      function-i2s_route: "/gAAAFJzMmk2ZHVhMW5pcAMDIwA="
-                      mca-identity: "a3cm"
-                    }
-                  }
-                ]
-                compatible: "mcaCluster,t8130"
-                device_type: "i2s"
-                function-switch_config: [
-                  "Cacm.3lc"
-                ]
-                interrupt-parent: " "
-                interrupts: 371
-                mca-identity: ".3lc"
-                reg: [
-                  {
-                    addr: 3833643008
-                    size: 16384
-                  }
-                  {
-                    addr: 3835838464
-                    size: 16384
-                  }
-                  {
-                    addr: 3835854848
-                    size: 16384
-                  }
-                ]
-              }
+              iop-audio-controller: {
+                AAPL,phandle: 264
+                children: [
+                  {
+                    audio-hp: {
+                      AAPL,phandle: 265
+                      children: [
+                        {
+                          audio-codec: {
+                            AAPL,phandle: 266
+                            children: [
+                            ]
+                            compatible: "audio-data,cs42l79"
+                            data-sources: [
+                              "HPMics"
+                            ]
+                            device-name: "HPMic"
+                            device-uid: "HPMic"
+                            device_type: "audio-data"
+                            isolated-audio-service-input: 300
+                            reg: [
+                              "}"
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-s"
+                      dma-channels: [
+                        "\""
+                        "\""
+                      ]
+                      dma-parent: 298
+                      external-power-provider: 298
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "iaph"
+                    }
+                  }
+                  {
+                    audio-leap-internal-loopback: {
+                      AAPL,phandle: 267
+                      children: [
+                        {
+                          audio-leap-internal-loopback: {
+                            AAPL,phandle: 268
+                            audio-stream-formatter: "pael"
+                            children: [
+                            ]
+                            compatible: "audio-data,external"
+                            data-sources: [
+                              "NonSecure MCA LEAP Loopback"
+                            ]
+                            device-name: "NonSecure MCA LEAP Loopback"
+                            device-uid: "NonSecure MCA LEAP Loopback"
+                            device_type: "leap-audio-data"
+                            reg: [
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,leap"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "!"
+                        "\""
+                        "\""
+                      ]
+                      dma-parent: 297
+                      external-power-provider: 297
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "blil"
+                    }
+                  }
+                  {
+                    audio-mca-loopback: {
+                      AAPL,phandle: 269
+                      children: [
+                        {
+                          audio-mca-loopback: {
+                            AAPL,phandle: 270
+                            children: [
+                            ]
+                            compatible: "audio-data,audio-loopback"
+                            data-sources: [
+                              "NonSecure MCA Loopback"
+                            ]
+                            device-name: "NonSecure MCA Loopback"
+                            device-uid: "NonSecure MCA Loopback"
+                            device_type: "audio-data"
+                            reg: [
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-ns"
+                      dma-channels: "AAAAACEAAAAAAAAAwAAAAGAAAAAAAAAAAAAAAAAAAAABAAAAIQAAAAAAAADAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAiAAAAAAAAAMAAAABgAAAAAAAAAAAAAAAAAAAAAQAAACIAAAAAAAAAwAAAAGAAAAAAAAAAAAAAAAAAAAA="
+                      dma-parent: 296
+                      external-power-provider: 296
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "kbpl"
+                    }
+                  }
+                  {
+                    audio-receiver: {
+                      AAPL,phandle: 271
+                      children: [
+                        {
+                          audio-receiver: {
+                            AAPL,phandle: 272
+                            children: [
+                            ]
+                            compatible: "audio-data,external"
+                            data-sources: [
+                              "r2pa"
+                              "Receiver"
+                            ]
+                            device-name: "Receiver"
+                            device-uid: "Receiver"
+                            device_type: "audio-data"
+                            reg: [
+                              "}"
+                              "0"
+                            ]
+                            registerWithPrimary: null
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "\""
+                      ]
+                      dma-parent: 296
+                      external-power-provider: 296
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "vcer"
+                    }
+                  }
+                  {
+                    audio-flicker: {
+                      AAPL,phandle: 273
+                      children: [
+                        {
+                          audio-flicker: {
+                            AAPL,phandle: 274
+                            children: [
+                            ]
+                            compatible: "audio-data,external"
+                            data-sources: [
+                              "Flicker"
+                            ]
+                            device-name: "Flicker"
+                            device-uid: "Flicker"
+                            device_type: "audio-data"
+                            reg: [
+                              "0"
+                            ]
+                            registerWithPrimary: null
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "\""
+                      ]
+                      dma-parent: 296
+                      external-power-provider: 296
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "kclf"
+                    }
+                  }
+                  {
+                    audio-s-leap-internal-loopback: {
+                      AAPL,phandle: 275
+                      children: [
+                        {
+                          audio-s-leap-internal-loopback: {
+                            AAPL,phandle: 276
+                            audio-stream-formatter: "pael"
+                            children: [
+                            ]
+                            compatible: "audio-data,external"
+                            data-sources: [
+                              "Secure MCA LEAP Loopback"
+                            ]
+                            device-name: "Secure MCA LEAP Loopback"
+                            device-uid: "Secure MCA LEAP Loopback"
+                            device_type: "leap-audio-data"
+                            reg: [
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,leap"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "!"
+                        "\""
+                        "\""
+                      ]
+                      dma-parent: 297
+                      external-power-provider: 297
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "blls"
+                    }
+                  }
+                  {
+                    lp-mic-device: {
+                      AAPL,phandle: 277
+                      children: [
+                      ]
+                      compatible: "iop-audio,lp-mic-device"
+                      device_type: "lp-mic-device"
+                      external-named-power-provider: "AppleCS42L79Audio"
+                      function-cm_power_change_notify: [
+                        "mspl"
+                      ]
+                      identifier: "iapl"
+                    }
+                  }
+                  {
+                    lp-mic-io-buffer-device: {
+                      AAPL,phandle: 278
+                      children: [
+                      ]
+                      compatible: "iop-audio,isolated-io-buffer-device"
+                      device_type: "lp-mic-io-buffer-device"
+                      exclave-assigned: null
+                      exclave-edk-endpoint: "("
+                      exclave-endpoint: "'"
+                      external-named-power-provider: "SharedDARTMapperProxy"
+                      identifier: "xpda"
+                      iommu-parent: "M"
+                      physical-descriptions: "APoAAIA+AABtY3BsDAAAAAgAAAAQBAAA"
+                    }
+                  }
+                  {
+                    siri-listening-device: {
+                      AAPL,phandle: 279
+                      children: [
+                      ]
+                      compatible: "iop-audio,client-manager-device"
+                      device_type: "siri-listening-device"
+                      external-named-power-provider: "AppleCS42L79Audio"
+                      function-cm_power_change_notify: [
+                        "slpl"
+                      ]
+                      identifier: " ial"
+                      publish-user-client: null
+                      supports-multiple-user-clients: null
+                    }
+                  }
+                  {
+                    lp-mic-injection-device: {
+                      AAPL,phandle: 280
+                      children: [
+                        {
+                          lp-mic-injection-device: {
+                            AAPL,phandle: 281
+                            children: [
+                            ]
+                            compatible: "audio-data,external"
+                            data-sources: [
+                              "jipl"
+                              "LPMic Injection"
+                            ]
+                            device-name: "LPMic Injection"
+                            device-uid: "LPMicInjection"
+                            device_type: "audio-data"
+                            reg: "AQIAAAQAAQAAG7cA7gIBABAAAQAPAAAAAAAAAAQAEAAAAAAA"
+                          }
+                        }
+                      ]
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "@"
+                        "\""
+                      ]
+                      dma-parent: 296
+                      external-power-provider: 296
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "jipl"
+                    }
+                  }
+                  {
+                    audio-speaker-mca: {
+                      AAPL,phandle: 282
+                      children: [
+                        {
+                          audio-speaker: {
+                            AAPL,phandle: 283
+                            children: [
+                            ]
+                            compatible: "audio-data,cs35l28"
+                            device_type: "audio-data"
+                            reg: [
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,mca"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "`"
+                        "!"
+                        "\""
+                        "`"
+                        "\""
+                      ]
+                      dma-parent: 296
+                      external-power-provider: 296
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "kpsm"
+                    }
+                  }
+                  {
+                    audio-speaker: {
+                      AAPL,phandle: 284
+                      children: [
+                      ]
+                      compatible: "audio-iop-speaker"
+                      device_type: "iop-audio-ns"
+                      iboot-audio-volume: 65407
+                      identifier: "rkps"
+                      input-data-source-selectors: "0Vps0Ips02vs0res0fis0fvs1Vps1Ips12vs1res1fis1fvs"
+                      output-data-source-selectors: "StoBSpoT"
+                      speaker-config-0: "IHBvdEdtY3D8BwAAEQAAAGxwcGmWAAAAPygKAA=="
+                      speaker-config-1: "IG10YkdtY3D5BwAAEQAAAGxwcGmWAAAAPygJAA=="
+                    }
+                  }
+                  {
+                    audio-haptic: {
+                      AAPL,phandle: 285
+                      audio-enable-warmup-ms: 3
+                      children: [
+                      ]
+                      compatible: "audio-control,audio-iop-haptics"
+                      device_type: "iop-audio-ns"
+                      function-hall_ctrl: [
+                        "llah"
+                      ]
+                      function-haptics_session: [
+                        "csph"
+                      ]
+                      function-power_peak_budget: [
+                        "wpkp"
+                      ]
+                      function-thermal_budget: [
+                        "reht"
+                      ]
+                      identifier: "chpa"
+                      input-latency: 8
+                      model-name: "leap"
+                      output-latency: 8
+                      peak-power-range: "RBYAACAFAABEFgAA"
+                      powered-on-state: "drwp"
+                      prewarm-on-state: " 1wp"
+                      thermal-budget-range: "MwsAAHcBAAAzCwAA"
+                      uid: "Actuator"
+                      zerofill-buffer-size-ms: 5
+                    }
+                  }
+                  {
+                    audio-haptic-transport: {
+                      AAPL,phandle: 286
+                      children: [
+                        {
+                          audio-haptic: {
+                            AAPL,phandle: 287
+                            audio-stream-formatter: "pael"
+                            children: [
+                            ]
+                            compatible: "audio-data,audio-iop-haptics"
+                            device_type: "leap-audio-data"
+                            reg: [
+                              "0"
+                              " "
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,leap"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "`"
+                        "\""
+                        "`"
+                      ]
+                      dma-parent: 297
+                      external-power-provider: 297
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: " hpa"
+                    }
+                  }
+                  {
+                    audio-hw-pcm-audiomgr: {
+                      AAPL,phandle: 288
+                      children: [
+                      ]
+                      compatible: "iop-audio,pcm-asset-manager-device"
+                      device_type: "iop-audio-ns"
+                      identifier: "Mmcp"
+                      kci-name: "AOPAudioHWPCMAssetManagerInterface"
+                    }
+                  }
+                  {
+                    audio-hpdbg: {
+                      AAPL,phandle: 289
+                      children: [
+                      ]
+                      compatible: "audio-control,audio-iop-haptic-debug"
+                      default-input-data-sources: "capacaocsopcbqes0Vra0Iraxlahylah"
+                      device_type: "iop-audio-ns"
+                      function-input-data-selectors: [
+                        "sidh"
+                      ]
+                      identifier: "cdha"
+                      input-data-source-selectors: "AAAAAGNhcGFjYW9hc29wYzBJcmEwVnJhY2FvY3N0bGYxY3BoZG1jaHhsYWh0dW9jcnhhaHBtdGNwbXRzMFZwczBJcHN1YXhtanJ0bW5leG0yY3BoM2NwaDRjcGhzcG1zYnFlc25lcG1lcG9hbmVwYW9jZGlpZGRpbWlsdnVhb2F1YXBheWxhaHJ5YWhmZmVjZG1jdnhzZXJ5c2VycG1yc3BtcnBwbXJjZG1jZzBWYXBhZ3BjdGNtc3RjbHNwZGN0b3BjdGNjY3RnbGN0MnZjdG11Y3RhZ3R0cG10eHBtdHlnd2xzZ3RsZnBtcnRmZm9zbmVvdHNvcGN3b3BzZ2NwYXRzZXh0c2V2dHNlYnRuaWJmcGhiMHRzdDF0c3QydHN0M3RzdHFyaWhxcmlhbmV2czF0bmkydG5pdGFidnRzYnYxYnBtMmJwbXhsZnJ4Y2ZmeGxmZnhjZnN0c2ZyY3NwYWNzb2FmdmxpaWcyYWNnMmFpdGNzY3Rjc2l0cnBjdHJwaXZhcGN2YXA1MmFwaXhtcGljYXA1MmNwaXdwc2N3cHNpd3BjY3dwY2l0Y3JjdGNydGNrMXlsZnJ5Y2ZmeWxmZnljZnN0ZzJh"
+                      input-latency: 5
+                      model-name: "IOPHapticDebug"
+                      output-latency: 5
+                      powered-on-state: "drwp"
+                      uid: "Haptic Debug"
+                      zerofill-buffer-size-ms: 5
+                    }
+                  }
+                  {
+                    audio-hpdbg-transport: {
+                      AAPL,phandle: 290
+                      children: [
+                        {
+                          audio-hpdbg: {
+                            AAPL,phandle: 291
+                            audio-stream-formatter: "pael"
+                            children: [
+                            ]
+                            compatible: "audio-data,audio-iop-hpdbg"
+                            device_type: "leap-audio-data"
+                            reg: [
+                              "0"
+                            ]
+                          }
+                        }
+                      ]
+                      clock-domain: "niam"
+                      compatible: "iop-adma-stream,leap"
+                      device_type: "iop-audio-ns"
+                      dma-channels: [
+                        "!"
+                        "\""
+                      ]
+                      dma-parent: 297
+                      external-power-provider: 297
+                      function-admac_powerswitch: [
+                        "CSPa"
+                      ]
+                      identifier: "dhpa"
+                    }
+                  }
+                  {
+                    audio-haptic-leap: {
+                      AAPL,phandle: 292
+                      children: [
+                      ]
+                      compatible: "iop-audio,haptics-leap-control-device"
+                      device_type: "iop-audio-ns"
+                      identifier: "cmpl"
+                      kci-name: "AppleHapticsAudioInterface"
+                      parking-node-id: "Nkrp"
+                      remote-node-interface: 293
+                    }
+                  }
+                  {
+                    audio-haptic-parking: {
+                      AAPL,phandle: 293
+                      children: [
+                      ]
+                      device_type: "iop-audio-ns"
+                      identifier: "Nkrp"
+                    }
+                  }
+                ]
+                compatible: "iop-audio,controller"
+                device_type: "iop-audio-controller"
+                iop-audio-service-name: "AOPAudioService"
+              }
             }
             {
-              alc0: {
-                AAPL,phandle: 261
-                alc-number: 0
-                children: [
-                  {
-                    audio-hpdbg: {
-                      AAPL,phandle: 262
-                      audio-stream-formatter: "pael"
-                      children: [
-                      ]
-                      compatible: "audio-data,aop-audio-hpdbg"
-                      device_type: "leap-audio-data"
-                      reg: "AEIAAAgAAQAAG7cA+gABADAAAQAAAAAA/wAAAAAIEBABAQAA"
-                    }
-                  }
-                ]
-                clock-domain: "niam"
-                compatible: "alc,t8130"
-                device_type: "i2s"
-                dma-channels: [
-                  "!"
-                  "\""
-                ]
-                dma-parent: 237
-                external-power-provider: [
-                  "A"
-                ]
-                function-admac_powerswitch: [
-                  "CSPa"
-                ]
-                function-aop-device-control: [
-                  "A"
-                  "ltCg"
-                ]
-                function-aop-device-control-id: "dhpa"
-              }
+              iop-voicetrigger-controller: {
+                AAPL,phandle: 294
+                children: [
+                  {
+                    audio-vt-device: {
+                      AAPL,phandle: 295
+                      children: [
+                      ]
+                      compatible: "iop-audio,isolated-vt-device"
+                      device_type: "iop-nub"
+                      exclave-assigned: null
+                      exclave-edk-endpoint: "+"
+                      exclave-endpoint: "*"
+                      identifier: "mctv"
+                    }
+                  }
+                ]
+                compatible: "iop-audio,controller"
+                device_type: "iop-voicetrigger-controller"
+                iop-audio-service-name: "AOPVoiceTriggerService"
+              }
             }
             {
-              alc2: {
-                AAPL,phandle: 263
-                alc-number: 2
-                children: [
-                  {
-                    audio-haptic: {
-                      AAPL,phandle: 264
-                      audio-stream-formatter: "pael"
-                      children: [
-                      ]
-                      compatible: "audio-data,aop-audio-haptic"
-                      device_type: "leap-audio-data"
-                      reg: "AEIAAAgAAQAAG7cA+gABADAAAQACAAAAAAAAAAEAEBACAQAA"
-                    }
-                  }
-                ]
-                clock-domain: "niam"
-                compatible: "alc,t8130"
-                device_type: "i2s"
-                dma-channels: [
-                  "!"
-                  "`"
-                  "\""
-                  "`"
-                ]
-                dma-parent: 237
-                external-power-provider: [
-                  "A"
-                ]
-                function-admac_powerswitch: [
-                  "CSPa"
-                ]
-                function-aop-device-control: [
-                  "A"
-                  "ltCg"
-                ]
-                function-aop-device-control-id: " hpa"
-              }
+              admac-base-ns: {
+                #dma-channels: 13
+                AAPL,phandle: 296
+                channel-buffer-alloc-base-rx: 0
+                channel-buffer-alloc-base-tx: 0
+                channel-buffer-allocation: "AB4AAAAAAAAAHgAAAAAAAA=="
+                channels-offset: 0
+                children: [
+                ]
+                clock-gates: 299
+                compatible: "admac,t8140"
+                device_type: "admac"
+                interrupt-parent: " "
+                interrupts: 449
+                iommu-parent: "K"
+                irq-destination-index: 0
+                irq-destinations: " CIAUPCA NTGDSNU"
+                reg: [
+                  {
+                    addr: 4353687552
+                    size: 212992
+                  }
+                  {
+                    addr: 4163534848
+                    size: 8
+                  }
+                ]
+                role: "SNAB"
+                service-exclave_proxy: null
+              }
             }
           ]
-          compatible: "arm-io,t8130"
+          compatible: "arm-io,t8140"
-          device_type: "t8130-io"
+          device_type: "t8140-io"
-          ranges: "AAAAAAAAAAAAAAAQAgAAAAAAAEABAAAAAAAAAAcAAAAAAAAABwAAAAAAAIADAAAAAAAAgAUAAAAAAACABQAAAAAAAIAAAAAAAAAAoAUAAAAAAACgBQAAAAAAACAAAAAAAAAAwAUAAAAAAADABQAAAAAAAEAAAAAAAAAAAAYAAAAAAAAABgAAAAAAAIAAAAAA"
+          ranges: "AAAAAAAAAAAAAAAQAgAAAAAAAPACAAAAAAAACAQAAAAAAAAIBAAAAAAAAAUAAAAAAAAAkAMAAAAAAACQAwAAAACABgcAAAAAAAAAsBwAAAAAAACwHAAAAAAAABAAAAAAAAAAwAsAAAAAAADACwAAAAAAACAAAAAAAAAAgAsAAAAAAACACwAAAAAAAEAAAAAAAAAAmAMAAAAAAACYAwAAAACABgcAAAAA"
-          soc-generation: "H16"
+          soc-generation: "H17"
         }
       }
       {
         buttons: {
+          function-button_capture: [
+            "q"
+            "RntbPACb"
+          ]
-          AAPL,phandle: 290
+          AAPL,phandle: 333
           button-names: [
+            "capture"
             ...
             ...
             ...
             ...
           ]
           function-button_hold: [
             ...
-            "s"
+            "q"
           ]
           function-button_ringeren: [
             ...
-            "s"
+            "q"
           ]
           function-button_voldown: [
             ...
-            "s"
+            "q"
           ]
           function-button_volup: [
             ...
-            "s"
+            "q"
           ]
         }
       }
     ]
     compatible: [
       ...
-      "D84AP"
-      "iPhone16,2"
+      "D93AP"
+      "iPhone17,1"
     ]
-    model: "iPhone16,2"
+    model: "iPhone17,1"
-    target-sub-type: "D84AP"
+    target-sub-type: "D93AP"
-    target-type: "D84"
+    target-type: "D93"
-    time-stamp: "Mon Sep 2 21:56:07 PDT 2024"
+    time-stamp: "Mon Sep 2 21:56:15 PDT 2024"
   }
 }
```