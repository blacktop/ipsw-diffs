## uia2unboxed

> Group: ⬆️ Updated

```diff

 				(require-not (require-any
 					(literal "/usr/local/bin/collectWiFiDebugInfo.sh")
 					(literal "/usr/local/bin/eventer")
+				))
+				(require-not (require-any
 					(literal "/usr/local/bin/gestalt_query")
+					(literal "/usr/local/bin/hkctl")
 				))
 				(require-not (literal "/usr/local/bin/CADebug"))
-				(require-not (literal "/usr/local/bin/hkctl"))
 			)
 			(require-not (system-attribute internal-build))
 		)
```
