ALTER TABLE  thai_provinces RENAME TO province;
ALTER TABLE  thai_amphures RENAME TO district;
ALTER TABLE  thai_tambons RENAME TO subdistrict;

ALTER TABLE province
DROP COLUMN geography_id;

UPDATE
    province
SET
    created_at = datetime('now'),
    updated_at = datetime('now');

UPDATE
    district
SET
    created_at = datetime('now'),
    updated_at = datetime('now');

UPDATE
    subdistrict
SET
    created_at = datetime('now'),
    updated_at = datetime('now');