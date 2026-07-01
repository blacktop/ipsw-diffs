# fileproviderd

Group: Updated

```diff

 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command
+		APFSIOC_DIR_STATS_OP
 		APFSIOC_GET_DIR_STATS_EXT
 		APFSIOC_GET_PURGEABLE_FILE_FLAGS
 		APFSIOC_GET_SPEC_TELEM
```
