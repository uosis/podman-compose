# SPDX-License-Identifier: GPL-2.0

import argparse
import unittest

from podman_compose import PodmanCompose
from podman_compose import compose_run_update_container_from_args


class TestComposeRunUpdateContainerFromArgs(unittest.TestCase):
    def test_minimal(self) -> None:
        cnt = get_minimal_container()
        compose = get_minimal_compose()
        args = get_minimal_args()

        compose_run_update_container_from_args(compose, cnt, args)

        expected_cnt = {"name": "default_name", "tty": True}
        self.assertEqual(cnt, expected_cnt)

    def test_additional_env_value_equals(self) -> None:
        cnt = get_minimal_container()
        compose = get_minimal_compose()
        args = get_minimal_args()
        args.env = ["key=valuepart1=valuepart2"]

        compose_run_update_container_from_args(compose, cnt, args)

        expected_cnt = {
            "environment": {
                "key": "valuepart1=valuepart2",
            },
            "name": "default_name",
            "tty": True,
        }
        self.assertEqual(cnt, expected_cnt)

    def test_publish_ports(self) -> None:
        cnt = get_minimal_container()
        compose = get_minimal_compose()
        args = get_minimal_args()
        args.publish = ["1111", "2222:2222"]

        compose_run_update_container_from_args(compose, cnt, args)

        expected_cnt = {
            "name": "default_name",
            "ports": ["1111", "2222:2222"],
            "tty": True,
        }
        self.assertEqual(cnt, expected_cnt)


def get_minimal_container() -> dict:
    return {}


def get_minimal_compose() -> PodmanCompose:
    compose = PodmanCompose()
    compose.project_name = "test_project"
    return compose


def get_minimal_args() -> argparse.Namespace:
    return argparse.Namespace(
        T=None,
        cnt_command=None,
        entrypoint=None,
        env=None,
        name="default_name",
        rm=None,
        service="test_service",
        publish=None,
        service_ports=None,
        user=None,
        volume=None,
        workdir=None,
    )
