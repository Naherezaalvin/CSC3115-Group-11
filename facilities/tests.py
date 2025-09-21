from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Facility


class FacilityModelTests(TestCase):

    def test_required_fields(self):
        facility = Facility()
        with self.assertRaises(ValidationError):
            facility.full_clean()

    def test_unique_name_location(self):
        Facility.objects.create(
            name="Maker Lab",
            location="Kampala",
            description="Test facility",
            facility_type="lab",
            capabilities="CNC"
        )
        with self.assertRaises(IntegrityError):
            Facility.objects.create(
                name="Maker Lab",
                location="Kampala",  # same name + location
                description="Another",
                facility_type="workshop",
                capabilities="PCB"
            )

    def test_delete_facility(self):
        facility = Facility.objects.create(
            name="Test Lab",
            location="Entebbe",
            description="To delete",
            facility_type="testing",
            capabilities="Materials"
        )
        facility_id = facility.id
        facility.delete()
        self.assertFalse(Facility.objects.filter(id=facility_id).exists())

    def test_capabilities_required_if_services_or_equipment(self):
        facility = Facility.objects.create(
            name="Innovation Hub",
            location="Jinja",
            description="With related items",
            facility_type="workshop",
            capabilities=""  # empty
        )

        # fake related sets
        class DummyQS:
            def exists(self): return True
            def count(self): return 1

        facility.services 
        facility.equipment

       
